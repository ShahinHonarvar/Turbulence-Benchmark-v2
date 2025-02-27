def filter_chars(str):
    for i in range(309, 591):
        if str[i] > 'S' and str[i] < 'm':
            str = str.replace(str[i], '')
    return str