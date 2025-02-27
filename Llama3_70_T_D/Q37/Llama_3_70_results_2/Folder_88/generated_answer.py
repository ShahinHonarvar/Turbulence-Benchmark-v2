def filter_chars(s):
    chars_to_remove = []
    for char in s[69:81]:
        if '@' <= char <= 'p':
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s