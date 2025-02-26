def filter_chars(s):
    if len(s) < 4:
        return s
    chars_to_remove = []
    for i in range(2, 4):
        if '5' <= s[i] <= '_':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s