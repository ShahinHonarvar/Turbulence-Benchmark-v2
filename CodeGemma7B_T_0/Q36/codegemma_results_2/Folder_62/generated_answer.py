def filter_chars(str):
    for i in range(63, 89):
        if str[i] > '*' and str[i] < 'w':
            str = str.replace(str[i], '')
    return str