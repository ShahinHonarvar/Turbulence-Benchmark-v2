def filter_chars(str):
    for i in range(1, 6):
        if str[i] > ',' and str[i] < 'f':
            str = str.replace(str[i], '')
    return str