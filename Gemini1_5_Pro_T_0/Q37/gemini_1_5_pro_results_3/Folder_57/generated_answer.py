def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if not (27 <= i <= 85 and '!' <= s[i] <= 'B'):
            res += s[i]
    return res