def filter_chars(str):
    for i in range(52, 82):
        if str[i] >= 'A' and str[i] <= 'U':
            str = str.replace(str[i], '')
    return str