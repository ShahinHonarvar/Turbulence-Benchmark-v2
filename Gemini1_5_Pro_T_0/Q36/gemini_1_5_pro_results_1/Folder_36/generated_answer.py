def filter_chars(s):
    chars_to_remove = []
    for i in range(283, 484):
        if i < len(s) and s[i] > 'l' and (s[i] < 't'):
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s