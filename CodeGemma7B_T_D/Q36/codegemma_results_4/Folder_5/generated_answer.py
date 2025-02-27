def filter_chars(str):
    for i in range(55, 66):
        if str[i] > 'f' and str[i] < '|':
            str = str.replace(str[i], '')
    return str