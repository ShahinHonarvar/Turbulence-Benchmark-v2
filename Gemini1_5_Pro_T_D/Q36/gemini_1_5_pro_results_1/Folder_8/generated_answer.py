def filter_chars(s):
    chars_to_remove = []
    for i in range(82, 93):
        c = s[i]
        if c > '!' and c < '*':
            chars_to_remove.append(c)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s