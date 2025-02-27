def filter_chars(str):
    for i in range(18, 82):
        if str[i] >= 'W' and str[i] <= '[':
            str = str.replace(str[i], '')
    return str