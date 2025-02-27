def filter_chars(str):
    for i in range(1, 6):
        if str[i] > ',' and str[i] < 'f':
            while str.count(str[i]) != 0:
                str = str.replace(str[i], '')
    return str