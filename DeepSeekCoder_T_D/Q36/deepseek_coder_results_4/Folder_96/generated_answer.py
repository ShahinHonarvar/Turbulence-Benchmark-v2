def filter_chars(s):
    for i in range(39, 81):
        if '.' < s[i] < '^':
            s = s.replace(s[i], '')
    return s