def filter_chars(s):
    filtered_str = []
    for i, c in enumerate(s):
        if 225 <= i <= 381 and 'D' <= c <= 'Y':
            continue
        filtered_str.append(c)
    return ''.join(filtered_str)