def filter_chars(s):
    for i in range(171, 636):
        if i < len(s) and 'c' < s[i] < 's':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s