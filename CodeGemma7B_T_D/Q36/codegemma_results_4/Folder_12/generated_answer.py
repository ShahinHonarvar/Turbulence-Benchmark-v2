def filter_chars(a):
    b = ''
    for c in a:
        if c > 'm' and c < 'w' and (c not in b):
            b += c
    return b