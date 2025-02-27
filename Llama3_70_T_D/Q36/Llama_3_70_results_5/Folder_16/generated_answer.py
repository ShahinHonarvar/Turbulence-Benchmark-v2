def filter_chars(s):
    chars_to_filter = set(s[331:713])
    filtered_chars = [c for c in chars_to_filter if 'M' < c < '_']
    for c in filtered_chars:
        s = s.replace(c, '')
    return s