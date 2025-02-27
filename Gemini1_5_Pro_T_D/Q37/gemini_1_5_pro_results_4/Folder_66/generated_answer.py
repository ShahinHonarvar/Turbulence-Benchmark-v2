def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if not (27 <= i <= 85 and 'c' <= s[i] <= 'i'):
            res += s[i]
    return res