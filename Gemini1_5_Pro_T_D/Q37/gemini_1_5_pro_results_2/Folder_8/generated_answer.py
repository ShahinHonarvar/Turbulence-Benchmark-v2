def filter_chars(s):
    for i in range(41, 87):
        if i < len(s) and 'S' <= s[i] <= 's':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s