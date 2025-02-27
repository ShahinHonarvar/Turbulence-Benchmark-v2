def filter_chars(s):
    for i in range(114, 640):
        if i < len(s) and '!' <= s[i] <= 'x':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s