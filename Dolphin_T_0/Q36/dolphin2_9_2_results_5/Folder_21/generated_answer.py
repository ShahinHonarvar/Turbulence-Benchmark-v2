def filter_chars(s):
    chars_to_remove = [s[i] for i in range(219, 403) if s[i] > '*' and s[i] < '7']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s