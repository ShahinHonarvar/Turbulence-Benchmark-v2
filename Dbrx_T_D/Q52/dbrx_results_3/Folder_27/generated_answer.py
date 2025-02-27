def palindrome_of_length_n(s):
    n = 56
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindromes = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] in palindromes:
            continue
        substring = ''.join(filter(english_letters.__contains__, s[i:i + n]))
        if len(substring) == n and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes