def filter_chars(s):
    for i in range(27, 75):
        chr = s[i]
        if 'A' < chr < 'i':
            s = s.replace(chr, '')
    return s