def filter_chars(str):
    for i in range(43, 59):
        if str[i] > '5' and str[i] < 'C':
            continue
        str = str.replace(str[i], '')
    return str