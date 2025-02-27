def filter_chars(s):
    for i in range(318, 337):
        if i < len(s) and 'B' < s[i] < 'z':
            c = s[i]
            s = ''.join([x for x in s if x != c])
    return s