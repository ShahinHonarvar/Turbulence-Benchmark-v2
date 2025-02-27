def filter_chars(str):
    str = list(str)
    for i in range(46, 74):
        if str[i] > '&' and str[i] < 'M':
            str[i] = '&'
    str = ''.join(str)
    return str