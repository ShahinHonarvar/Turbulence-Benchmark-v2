def palindrome_of_length_n(string):
    string = string.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindrome_set = set()
    for i in range(len(string) - 16 + 1):
        substring = string[i:i + 16]
        if set(substring).issubset(english_letters) and substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set