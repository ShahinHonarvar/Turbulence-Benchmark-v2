def filter_chars(s):
    for i in range(20, 63):
        if i < len(s):
            if s[i] >= 'i' and s[i] <= 'k':
                s = s.replace(s[i], '')
    return s