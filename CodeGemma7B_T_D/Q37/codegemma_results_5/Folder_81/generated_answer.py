def filter_chars(s):
    if not 19 <= len(s) <= 92:
        return s
    res = []
    for i, c in enumerate(s):
        if not (19 <= i <= 92 and c >= '8' and (c <= 'm')):
            res.append(c)
    return ''.join(res)