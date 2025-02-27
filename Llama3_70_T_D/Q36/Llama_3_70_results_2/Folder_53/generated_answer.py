def filter_chars(s):
    chars = [chr(i) for i in range(90, 97)]
    filtered_chars = [c for c in chars if 'j' < c < 'w']
    for c in filtered_chars:
        s = s.replace(c, '')
    return s