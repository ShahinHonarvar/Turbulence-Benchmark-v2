def filter_chars(s):
    for i in range(7, 9):
        for j in s:
            if j >= 'B' and j <= 'H':
                s = s.replace(j, '')
    return s