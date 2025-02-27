def filter_chars(a):
    s = list(a)
    for i in range(61, 88):
        if s[i] > '%' and s[i] < 'q':
            s.remove(s[i])
    return ''.join(s)