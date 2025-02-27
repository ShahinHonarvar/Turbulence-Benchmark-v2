def filter_chars(s):
    chars_to_remove = []
    for i in range(51, 91):
        if s[i] > 'A' and s[i] < 'Q':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s