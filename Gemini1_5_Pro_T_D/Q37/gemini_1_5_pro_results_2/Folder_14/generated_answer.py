def filter_chars(s):
    for i in range(35, 99):
        if i < len(s) and 'A' <= s[i] <= 'b':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s