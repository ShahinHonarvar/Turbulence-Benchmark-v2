def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if not (25 <= i <= 97 and 'm' <= s[i] <= 'w'):
            res += s[i]
    return res