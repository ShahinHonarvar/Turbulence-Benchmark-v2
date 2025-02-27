def filter_chars(str):
    for i in range(3, 5):
        if str[i] > 'Y' and str[i] < 's':
            str = str.replace(str[i], '')
    return str