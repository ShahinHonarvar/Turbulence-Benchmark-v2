def filter_chars(s):
    for i in range(32, 47):
        if '0' <= chr(i) <= 'k':
            s = ''.join((c for c in s if c != chr(i)))
    return s