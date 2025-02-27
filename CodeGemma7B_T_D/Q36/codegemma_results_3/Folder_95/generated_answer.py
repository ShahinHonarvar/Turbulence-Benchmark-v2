def filter_chars(str):
    for i in range(56, 86):
        if str[i] > '+' and str[i] < 'w':
            str = str.replace(str[i], '')
    return str