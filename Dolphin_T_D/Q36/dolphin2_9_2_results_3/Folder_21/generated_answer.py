def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if 219 <= i < 403 and s[i] > '*' and (s[i] < '7'):
            res = res + s.replace(s[i], '')
        else:
            res = res + s[i]
    return res