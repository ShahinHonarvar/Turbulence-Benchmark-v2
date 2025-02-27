def palindromes_of_specific_lengths(s):
    s = ''.join([c for c in s[27:96] if c.isalpha()]).lower()
    palindromes = set()
    for length in range(49, 52):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes