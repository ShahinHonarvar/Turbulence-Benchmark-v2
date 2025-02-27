def filter_chars(str):
    for i in range(13, 29):
        if str[i] >= 'c' and str[i] <= 'n':
            str[i] = ''
    return str