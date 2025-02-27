def palindromes_of_specific_lengths(s):
    s = s[106:281]
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            substring = ''.join((c for c in substring if c.isalpha()))
            substring = substring.lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes