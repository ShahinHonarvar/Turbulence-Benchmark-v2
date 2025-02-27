def filter_chars(s):
    chars_to_remove = []
    for i in range(23, 83):
        if s[i] and s[i] > 'f' and (s[i] < 'o'):
            chars_to_remove.append(s[i])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s