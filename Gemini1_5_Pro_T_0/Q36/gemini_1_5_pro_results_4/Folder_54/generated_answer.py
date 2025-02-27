def filter_chars(s):
    for i in range(18, 38):
        if i < len(s) and ')' < s[i] < 'P':
            c = s[i]
            s = s.replace(c, '')
    return s