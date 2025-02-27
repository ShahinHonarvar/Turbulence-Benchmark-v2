def filter_chars(s):
    chars_to_remove = []
    for i in range(35, 99):
        char = s[i]
        if 'A' <= char <= 'b' and char not in chars_to_remove:
            chars_to_remove.append(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s