def filter_chars(s):
    for i in range(34, 68):
        if i < len(s) and 'W' <= s[i] <= 'x':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s