def filter_chars(s):
    for i in range(3, 5):
        if i < len(s) and 'Y' < s[i] < 's':
            s = s.replace(s[i], '')
    return s