def filter_chars(s):
    res = []
    for i in range(len(s)):
        if not (477 <= i <= 984 and ',' <= s[i] <= 'V'):
            res.append(s[i])
    return ''.join(res)