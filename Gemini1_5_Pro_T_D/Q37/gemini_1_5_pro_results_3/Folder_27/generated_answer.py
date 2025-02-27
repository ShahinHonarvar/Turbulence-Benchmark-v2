def filter_chars(s):
    for i in range(43, 81):
        if i < len(s) and s[i] >= '=' and (s[i] <= 'E'):
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s