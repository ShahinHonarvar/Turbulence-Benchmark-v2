def filter_chars(s):
    for i in range(1, len(s) - 1):
        if '-' < s[i] < 'L':
            s = s.replace(s[i], '')
    return s