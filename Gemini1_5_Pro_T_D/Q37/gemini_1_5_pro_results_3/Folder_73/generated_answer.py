def filter_chars(s):
    for i in range(22, 86):
        if i <= len(s) - 1:
            if s[i] >= '7' and s[i] <= 'e':
                s = s.replace(s[i], '')
    return s