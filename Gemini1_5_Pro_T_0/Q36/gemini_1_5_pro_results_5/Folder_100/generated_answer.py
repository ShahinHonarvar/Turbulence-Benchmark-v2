def filter_chars(s):
    chars_to_remove = []
    for i in range(44, 69):
        if i < len(s) and s[i] > 'B' and (s[i] < 'r'):
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s