def filter_chars(s):
    chars_to_remove = []
    for i in range(90, 97):
        if s[i] > 'j' and s[i] < 'w':
            chars_to_remove.append(s[i])
    for c in chars_to_remove:
        s = s.replace(c, '')
    return s