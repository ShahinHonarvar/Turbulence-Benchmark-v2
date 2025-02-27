def filter_chars(s):
    chars_to_remove = []
    for i in range(25, 37):
        if i < len(s) and s[i] > 'A' and (s[i] < 'h'):
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s