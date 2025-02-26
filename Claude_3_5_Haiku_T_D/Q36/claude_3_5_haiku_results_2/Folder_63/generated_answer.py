def filter_chars(s):
    chars_to_remove = []
    for i in range(26, 80):
        if i < len(s) and '<' < s[i] < '>':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s