def filter_chars(s):
    if len(s) <= 18:
        return s
    for i in range(19, min(len(s), 38)):
        if ')' < s[i] < 'P':
            s = s.replace(s[i], '')
    return s