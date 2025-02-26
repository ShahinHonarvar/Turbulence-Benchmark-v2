def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[15:87]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 51, min(i + 61, len(substring) + 1)):
            substr = substring[i:j]
            if substr == substr[::-1] and 51 <= len(substr) <= 60:
                result.add(substr)
    return result