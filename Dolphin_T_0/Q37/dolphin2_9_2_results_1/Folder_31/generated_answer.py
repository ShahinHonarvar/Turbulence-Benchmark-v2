def filter_chars(s):
    new_s = ''
    for i, c in enumerate(s):
        if 57 <= i <= 96 and '<' <= c <= 'w':
            continue
        new_s += c
    return new_s