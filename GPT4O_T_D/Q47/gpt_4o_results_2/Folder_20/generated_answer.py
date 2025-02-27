def palindromes_of_specific_lengths(s):
    s = ''.join([c.lower() for c in s[20:75] if c.isalpha()])
    palindromes = set()
    for length in range(36, 43):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes