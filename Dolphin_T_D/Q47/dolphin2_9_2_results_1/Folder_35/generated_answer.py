def palindromes_of_specific_lengths(s: str) -> set:
    s = s[33:91]
    palindromes = set()
    for length in range(14, 40):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            sub = ''.join((c.lower() for c in sub if c.isalpha()))
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes