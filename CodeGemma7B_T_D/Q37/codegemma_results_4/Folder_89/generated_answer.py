def filter_chars(str):
    new_str = ''
    for i, c in enumerate(str):
        if i >= 11 and i <= 32 and (c >= '!') and (c <= '@'):
            continue
        new_str += c
    return new_str