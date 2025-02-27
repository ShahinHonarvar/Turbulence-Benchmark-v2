def filter_chars(s):
    for i in range(83, 89):
        if '*' < s[i] < '[':
            s = s.replace(s[i], '')
    return s