def filter_chars(s):
    chars_to_remove = [s[i] for i in range(83, 100) if s[i] >= '*' and s[i] <= 'j']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s