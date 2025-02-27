def filter_chars(s):
    for i in range(20, 63):
        if i < len(s):
            if 'i' <= s[i] <= 'k':
                char_to_remove = s[i]
                s = s.replace(char_to_remove, '')
    return s