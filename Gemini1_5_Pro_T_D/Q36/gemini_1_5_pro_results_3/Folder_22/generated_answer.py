def filter_chars(s):
    chars_to_remove = []
    for i in range(55, 84):
        if i < len(s) and s[i] > ';' and (s[i] < 'z'):
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s