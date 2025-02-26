def filter_chars(s):
    chars_to_remove = []
    for i in range(5, 8):
        if '1' < s[i] < 'J':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s