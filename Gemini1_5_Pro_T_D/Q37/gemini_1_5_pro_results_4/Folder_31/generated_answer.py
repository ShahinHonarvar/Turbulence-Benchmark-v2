def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if not (57 <= i <= 96 and '<' <= s[i] <= 'w'):
            res += s[i]
    return res