def filter_chars(s):
    chars_to_remove = [s[i] for i in range(55, 84) if s[i] > ';' and s[i] < 'z']
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s