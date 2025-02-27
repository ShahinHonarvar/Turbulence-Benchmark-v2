def filter_chars(str):
    for i in range(70, 74):
        if str[i] > 'A' and str[i] < 'U':
            str = str.replace(str[i], '')
    return str