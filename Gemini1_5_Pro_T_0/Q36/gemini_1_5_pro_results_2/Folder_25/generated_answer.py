def filter_chars(s):
    chars_to_remove = []
    for i in range(24, 37):
        if i < len(s) and 'A' < s[i] < 'h':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s