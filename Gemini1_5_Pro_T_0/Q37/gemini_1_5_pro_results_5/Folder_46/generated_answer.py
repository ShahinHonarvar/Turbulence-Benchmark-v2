def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if not (11 <= i <= 72 and 'i' <= s[i] <= 'v'):
            res += s[i]
    return res