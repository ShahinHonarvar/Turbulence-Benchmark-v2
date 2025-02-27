def filter_chars(s):
    for i in range(2, 7):
        if i < len(s) and '3' < s[i] < '^':
            s = s.replace(s[i], '')
    return s