def filter_chars(s):
    new_s = ''
    for i, c in enumerate(s):
        if i < 51 or i > 96 or c < 'X' or (c > 'p'):
            new_s += c
    return new_s