def palindrome_of_length_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    if n < 186:
        return palindromes
    for i in range(n - 185):
        for j in range(i + 186, n + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    for c in 'abcdefghijklmnopqrstuvwxyz':
        for i in range(n - 185):
            for j in range(i + 186, n + 1):
                substring = s[i:j]
                if substring.replace(c.lower(), '').replace(c.upper(), '') == substring[::-1].replace(c.lower(), '').replace(c.upper(), ''):
                    palindromes.add(substring)
    return palindromes