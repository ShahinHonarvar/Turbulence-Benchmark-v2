def filter_chars(chars):
    for i in range(14, 75):
        if '9' < chars[i] < 'K':
            chars = chars.replace(chars[i], '')
    return chars