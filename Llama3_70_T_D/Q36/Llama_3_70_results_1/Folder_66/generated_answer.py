def filter_chars(s):
    s = list(s)
    for i in range(39, 87):
        c = chr(i)
        if '!' < c < '}':
            s = [x for x in s if x != c]
    return ''.join(s)