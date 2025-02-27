def filter_chars(s):
    for i in range(71, 97):
        if chr(i) >= '_' and chr(i) <= 'o':
            s = s.replace(chr(i), '')
    return s