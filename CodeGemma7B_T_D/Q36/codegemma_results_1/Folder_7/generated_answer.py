def filter_chars(st):
    while len(st) > 502:
        for i in range(502, 946):
            if st[i] > 'W' and st[i] < 'y':
                st = st[:i] + st[i + 1:]
    return st