def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[17:96]
    substring = ''.join((c.lower() for c in substring if c.isalpha()))
    n = len(substring)
    for i in range(n):
        for j in range(i + 12, min(i + 49, n)):
            if j - i + 1 > 49:
                break
            substr = substring[i:j + 1]
            if substr == substr[::-1] and 13 <= len(substr) <= 49:
                result.add(substr)
    return result