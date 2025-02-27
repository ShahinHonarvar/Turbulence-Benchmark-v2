def filter_chars(s):
    for i in range(51, 97):
        if chr(i) >= 'X' and chr(i) <= 'p':
            s = s.replace(chr(i), '')
    return s