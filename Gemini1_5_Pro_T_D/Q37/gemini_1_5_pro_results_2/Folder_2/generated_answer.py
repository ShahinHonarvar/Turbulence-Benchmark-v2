def filter_chars(s):
    new_s = ''
    for i, char in enumerate(s):
        if 477 <= i <= 984 and ',' <= char <= 'V':
            continue
        else:
            new_s += char
    return new_s