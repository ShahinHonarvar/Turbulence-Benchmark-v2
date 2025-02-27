def filter_chars(s):
    start = 46
    end = 91
    for i in range(start, end):
        if 'D' < s[i] < 'H':
            to_remove = s[i]
            s = s.replace(to_remove, '')
    return s