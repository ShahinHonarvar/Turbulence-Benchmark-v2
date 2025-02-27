def filter_chars(s):
    chars_to_filter = s[7:9]
    for char in chars_to_filter:
        if '6' <= char <= 'w':
            s = s.replace(char, '')
    return s