def palindromes_of_specific_lengths(s):
    s = s[24:85]
    res = set()
    for i in range(21, 32):
        for j in range(len(s) - i + 1):
            if s[j:j + i].lower() == s[j:j + i].lower()[::-1] and s[j:j + i].isalpha():
                res.add(s[j:j + i])
    return res