def palindromes_of_specific_lengths(s):
    s = s[24:85]
    res = set()
    for length in range(21, 32):
        for i in range(len(s) - length + 1):
            if s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                temp = ''.join(filter(str.isalpha, s[i:i + length]))
                res.add(temp)
    return res