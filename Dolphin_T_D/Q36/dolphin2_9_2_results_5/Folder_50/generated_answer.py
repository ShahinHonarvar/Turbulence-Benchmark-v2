def filter_chars(s):
    for i in range(61, 88):
        c = s[i]
        if c > '%' and c < 'q':
            s = ''.join([x for x in s if x != c])
    return s