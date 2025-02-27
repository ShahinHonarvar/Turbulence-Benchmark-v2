def filter_chars(s):
    chars_to_remove = [s[i] for i in range(3, 5) if s[i] > 'Y' and s[i] < 's']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s