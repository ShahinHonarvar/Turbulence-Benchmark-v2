def filter_chars(str):
    for i in range(283, 484):
        if str[i] > 'l' and str[i] < 't':
            str = str.replace(str[i], '')
    return str