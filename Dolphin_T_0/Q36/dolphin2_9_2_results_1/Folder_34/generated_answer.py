def filter_chars(s):
    chars_to_remove = [s[i] for i in range(10, 79) if s[i] > '?' and s[i] < 'm']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s