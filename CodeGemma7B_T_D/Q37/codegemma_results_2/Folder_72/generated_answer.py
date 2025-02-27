def filter_chars(s):
    res = list(s)
    for i in range(35, 52):
        for c in res[:]:
            if c == chr(i):
                res.remove(c)
    return ''.join(res)