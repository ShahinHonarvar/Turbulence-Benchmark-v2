def filter_chars(s):
    for i in range(19, 38):
        if ')' < s[i] < 'P':
            s = s.replace(s[i], '')
    return s