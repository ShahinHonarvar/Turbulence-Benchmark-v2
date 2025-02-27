def filter_chars(s):
    res = list(s)
    for i in range(31, 70):
        if res[i] > 'B' and res[i] < 'v':
            res = [char for char in res if char != res[i]]
    return ''.join(res)