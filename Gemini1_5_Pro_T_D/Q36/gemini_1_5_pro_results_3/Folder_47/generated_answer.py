def filter_chars(s):
    chars_to_remove = []
    for i in range(45, 57):
        if i >= len(s):
            break
        if s[i] > 'F' and s[i] < 'n':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s