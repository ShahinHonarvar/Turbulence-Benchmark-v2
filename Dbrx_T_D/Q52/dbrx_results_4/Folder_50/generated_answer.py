def palindrome_of_length_n(s):
    n = 40
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if set(substring) <= english_letters:
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes