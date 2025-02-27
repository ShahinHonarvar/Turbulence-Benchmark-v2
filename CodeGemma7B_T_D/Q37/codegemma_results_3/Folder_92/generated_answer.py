def filter_chars(s):
    filtered_s = ''
    for i, c in enumerate(s):
        if 4 <= i <= 4 and '7' <= c <= 'o':
            pass
        else:
            filtered_s += c
    return filtered_s