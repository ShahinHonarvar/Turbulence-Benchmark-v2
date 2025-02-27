def insert_before_character(s):
    res = []
    for c in s:
        if c == 'i':
            res.append('0')
        res.append(c)
    return ''.join(res)