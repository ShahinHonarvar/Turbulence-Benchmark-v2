def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[41:90]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    for i in range(len(substring)):
        for j in range(i + 23, min(i + 39, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate == candidate[::-1] and 23 <= len(candidate) <= 38:
                result.add(candidate)
    return result