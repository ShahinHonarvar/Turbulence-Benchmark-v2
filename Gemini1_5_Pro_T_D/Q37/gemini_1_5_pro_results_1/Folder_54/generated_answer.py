def filter_chars(s):
    for i in range(46, 86):
        if i < len(s) and '-' <= s[i] <= 'X':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s