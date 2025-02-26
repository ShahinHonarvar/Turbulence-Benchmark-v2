def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[12:123]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 12, min(i + 221, len(substring) + 1)):
            substr = substring[i:j]
            if substr == substr[::-1] and 12 <= len(substr) <= 220:
                result.add(substr)
    return result