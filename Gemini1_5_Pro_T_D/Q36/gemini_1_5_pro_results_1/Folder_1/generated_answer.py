def filter_chars(s):
    chars_to_remove = []
    for i in range(69, 87):
        if i >= len(s):
            break
        if s[i] > '#' and s[i] < 'L':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s