def filter_chars(s):
    chars_to_filter = s[10:15]
    for char in chars_to_filter:
        if 't' < char < 'v':
            s = s.replace(char, '')
    return s