def palindromes_of_specific_lengths(s):
    result = set()
    s = ''.join((c.lower() for c in s[130:296] if c.isalpha()))
    for i in range(len(s)):
        for j in range(i + 103, min(i + 159, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result