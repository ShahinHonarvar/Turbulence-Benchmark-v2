def palindrome_of_length_n(string):
    string = string.lower()
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    length_of_pal = 20
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + length_of_pal, len(string) + 1):
            substring = string[i:j]
            if set(substring).issubset(english_letters) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes