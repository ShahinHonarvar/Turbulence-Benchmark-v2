def palindromes_of_specific_lengths(s):
    result = set()
    substring = ''.join((c for c in s[35:89] if c.isalpha())).lower()
    for length in range(24, 34):
        for start in range(len(substring) - length + 1):
            portion = substring[start:start + length]
            if portion == portion[::-1]:
                result.add(portion)
    return result