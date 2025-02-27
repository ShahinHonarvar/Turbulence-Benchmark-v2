def filter_chars(s):
    chars = list(s)
    for i in range(331, 713):
        c = chars[i]
        if 'M' < c < '_':
            chars = [x for x in chars if x != c]
    return ''.join(chars)