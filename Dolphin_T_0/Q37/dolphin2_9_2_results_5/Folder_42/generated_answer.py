def filter_chars(s):
    new_s = ''
    for i, c in enumerate(s):
        if i not in range(73, 75) or 'U' <= c <= 'l':
            new_s += c
    return new_s