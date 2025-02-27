def palindromes_of_specific_lengths(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    s = s[10:75]
    res = set()
    for start in range(len(s)):
        for length in range(6, 9):
            if start + length <= len(s):
                segment = s[start:start + length]
                if segment == segment[::-1]:
                    res.add(s[start:start + length])
    return res