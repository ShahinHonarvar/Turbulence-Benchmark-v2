def palindrome_of_length_n(s):
    n = 91
    letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if set(substring) <= letters:
            if substring == substring[::-1]:
                palindromes.add(substring.lower())
    return palindromes