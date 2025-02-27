def filter_chars(s):
    chars_to_filter = [s[i] for i in range(1, 6) if ',' < s[i] < 'f']
    for c in chars_to_filter:
        s = s.replace(c, '')
    return s