def filter_chars(s):
    res = ''
    for i in range(len(s)):
        if i in range(12, 78) and s[i] >= ':' and (s[i] <= 'L'):
            continue
        else:
            res += s[i]
    return res