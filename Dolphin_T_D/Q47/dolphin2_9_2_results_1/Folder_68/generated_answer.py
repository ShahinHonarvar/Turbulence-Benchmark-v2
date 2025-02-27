def palindromes_of_specific_lengths(s):
    s = ''.join((char.lower() for char in s if char.isalpha()))[:50]
    res = set()
    for i in range(50, 101):
        for j in range(len(s) - i + 1):
            if s[j:j + i] == s[j:j + i][::-1]:
                res.add(s[j:j + i])
    return res