def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join((c.lower() for c in s if c.isalpha()))[:301]
    for i in range(len(s)):
        for j in range(i + 50, min(i + 61, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result