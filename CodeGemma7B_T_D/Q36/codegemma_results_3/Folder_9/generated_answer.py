def filter_chars(str):
    for i in range(50, 92):
        if str[i] > 'A' and str[i] < 'Q':
            str = str.replace(str[i], '')
    return str