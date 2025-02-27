def filter_chars(s):
    chars_to_remove = [s[i] for i in range(27, 30) if s[i] >= ';' and s[i] <= 'b']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s