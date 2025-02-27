def filter_chars(s):
    for i in range(86, 93):
        if i < len(s) and '!' <= s[i] <= 's':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s