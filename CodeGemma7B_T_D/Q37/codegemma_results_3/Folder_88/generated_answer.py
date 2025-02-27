def filter_chars(s):
    new_s = []
    for i, c in enumerate(s):
        if i >= 69 and i <= 80 and (c >= '@') and (c <= 'p'):
            continue
        new_s.append(c)
    return ''.join(new_s)