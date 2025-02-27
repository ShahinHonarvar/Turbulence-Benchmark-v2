def filter_chars(s):
    for i in range(12, 26):
        if i < len(s) and 'P' <= s[i] <= 'x':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s