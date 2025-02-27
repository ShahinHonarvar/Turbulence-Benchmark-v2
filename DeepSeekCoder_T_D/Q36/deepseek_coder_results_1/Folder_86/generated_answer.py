def filter_chars(s):
    for i in range(673, 709):
        if 'X' < s[i] < '}':
            s = s.replace(s[i], '')
    return s