def filter_chars(s):
    for i in range(41, 80):
        if i < len(s) and 'f' <= s[i] <= '|':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s