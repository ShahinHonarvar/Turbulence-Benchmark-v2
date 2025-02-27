def filter_chars(s):
    chars_to_remove = []
    for i in range(29, 33):
        if s[i] > '%' and s[i] < 'a':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s