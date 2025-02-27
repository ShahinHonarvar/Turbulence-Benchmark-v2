def filter_chars(s):
    chars_to_remove = []
    for i in range(55, 91):
        if s[i] > 'J' and s[i] < 'X':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s