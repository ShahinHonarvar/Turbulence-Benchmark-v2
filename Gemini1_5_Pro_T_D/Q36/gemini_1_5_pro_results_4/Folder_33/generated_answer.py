def filter_chars(s):
    chars_to_remove = []
    for i in range(300, 418):
        c = s[i]
        if c > '9' and c < 'P':
            chars_to_remove.append(c)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s