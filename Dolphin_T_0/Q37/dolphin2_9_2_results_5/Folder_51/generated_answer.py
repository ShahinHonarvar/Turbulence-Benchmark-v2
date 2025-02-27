def filter_chars(s):
    chars_to_remove = [s[i] for i in range(36, 41) if s[i] >= 'H' and s[i] <= 'e']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s