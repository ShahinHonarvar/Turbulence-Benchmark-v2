def filter_chars(s):
    filtered = ''
    for i, c in enumerate(s):
        if 69 < i < 97 and 'V' < c < 'j':
            continue
        filtered += c
    return filtered