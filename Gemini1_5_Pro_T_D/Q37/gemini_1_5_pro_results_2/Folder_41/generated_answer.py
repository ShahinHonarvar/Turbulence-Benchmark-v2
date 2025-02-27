def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if not (26 <= i <= 64 and 'V' <= s[i] <= 'o'):
            res += s[i]
    return res