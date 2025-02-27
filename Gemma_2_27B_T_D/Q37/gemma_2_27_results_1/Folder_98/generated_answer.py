def filter_chars(s):
    res = []
    for i, char in enumerate(s):
        if 8 <= i <= 9 and 'R' <= char <= 't':
            s = s.replace(char, '')
        res.append(char)
    return ''.join(res)