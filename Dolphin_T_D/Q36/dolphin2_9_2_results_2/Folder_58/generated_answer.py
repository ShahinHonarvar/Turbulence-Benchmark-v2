def filter_chars(s):
    result = list(s)
    for i in range(318, 337):
        c = s[i]
        if 'B' < c < 'z':
            result = [x for x in result if x != c]
    return ''.join(result)