def filter_chars(s):
    chars_to_remove = []
    for i in range(54, 84):
        if s[i] >= 'j' and s[i] <= 'v':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s