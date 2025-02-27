def palindromes_of_specific_lengths(s):
    s = s[27:78]
    s = ''.join([c.lower() for c in s if c.isalpha()])
    palindromes = set()
    for i in range(len(s) - 18):
        for j in range(18, 20):
            substring = s[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes