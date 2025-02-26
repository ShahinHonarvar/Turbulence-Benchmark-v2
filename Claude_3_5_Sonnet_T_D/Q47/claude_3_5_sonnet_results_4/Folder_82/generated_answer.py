def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join((c.lower() for c in s if c.isalpha()))
    for i in range(3, min(301, len(s))):
        for j in range(i, min(301, len(s))):
            substring = s[i:j + 1]
            if 30 <= len(substring) <= 300 and substring == substring[::-1]:
                result.add(substring)
    return result