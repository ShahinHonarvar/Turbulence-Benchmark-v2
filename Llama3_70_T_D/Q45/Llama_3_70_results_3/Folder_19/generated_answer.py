def palindromes_between_indices(s):
    s = s[1:8].lower()
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = set()
    for length in range(7, len(s) + 1):
        for start in range(len(s) - length + 1):
            substr = s[start:start + length]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes