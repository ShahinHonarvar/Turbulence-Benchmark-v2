def filter_chars(s):
    for i in range(770, 971):
        if i < len(s) and '-' <= s[i] <= 'D':
            char_to_remove = s[i]
            s = s.replace(char_to_remove, '')
    return s