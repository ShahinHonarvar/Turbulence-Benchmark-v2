def palindrome_of_length_at_least_n(s):
    s = ''.join((e.lower() for e in s if e.isalpha()))
    palindromes = set()
    for i in range(len(s) - 100 + 1):
        for j in range(100):
            substring = s[i:i + j + 1]
            if substring == substring[::-1] and len(substring) >= 100:
                palindromes.add(substring)
    return palindromes