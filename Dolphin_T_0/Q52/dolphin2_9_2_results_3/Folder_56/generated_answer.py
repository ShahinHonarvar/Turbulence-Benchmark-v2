def palindrome_of_length_n(string):
    string = string.lower()
    letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(string) - 94):
        substring = string[i:i + 95]
        if set(substring).issubset(letters) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes