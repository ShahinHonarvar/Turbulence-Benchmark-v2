def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[41:90]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 39, len(substring) + 1)):
            substr = substring[i:j]
            if substr == substr[::-1] and 23 <= len(substr) <= 38:
                result.add(substr)
    return result