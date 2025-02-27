def filter_chars(s):
    chars_to_remove = []
    for i in range(421, 854):
        if i < len(s) and s[i] > 'D' and (s[i] < 'J'):
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s