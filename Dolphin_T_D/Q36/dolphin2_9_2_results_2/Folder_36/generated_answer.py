def filter_chars(s):
    chars_to_remove = [s[i] for i in range(283, 484) if 'l' < s[i] < 't']
    for c in set(chars_to_remove):
        s = s.replace(c, '')
    return s