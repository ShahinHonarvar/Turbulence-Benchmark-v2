def filter_chars(s):
    for i in range(13, 29):
        if i < len(s) and 'c' <= s[i] <= 'n':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s