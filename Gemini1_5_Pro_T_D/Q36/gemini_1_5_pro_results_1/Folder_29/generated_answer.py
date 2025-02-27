def filter_chars(s):
    chars_to_remove = []
    for i in range(46, 68):
        if i >= len(s):
            break
        if s[i] > 'H' and s[i] < 's':
            chars_to_remove.append(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s