def filter_chars(s):
    chars_to_remove = []
    for i in range(16, 85):
        if 'I' < s[i] < 'M':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s