def filter_chars(s):
    chars_to_remove = []
    for i in range(42, 98):
        if i < len(s) and '*' <= s[i] <= 'b':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s