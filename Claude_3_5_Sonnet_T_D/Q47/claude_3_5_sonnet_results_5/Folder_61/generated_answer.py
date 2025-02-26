def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join((c.lower() for c in s if c.isalpha()))[:31]
    for i in range(len(s)):
        for j in range(i + 20, min(i + 31, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and 20 <= len(substring) <= 30:
                result.add(substring)
    return result