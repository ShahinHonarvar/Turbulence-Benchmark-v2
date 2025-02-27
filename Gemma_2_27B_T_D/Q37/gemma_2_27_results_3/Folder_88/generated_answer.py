def filter_chars(s):
    for i in range(69, 81):
        if i < len(s):
            char = s[i]
            if char >= '@' and char <= 'p':
                s = s.replace(char, '')
    return s