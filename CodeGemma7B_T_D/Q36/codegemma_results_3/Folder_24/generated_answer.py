def filter_chars(str):
    for i in range(10, 15):
        if str[i] > 't' and str[i] < 'v':
            str = str[:i] + str[i + 1:]
    return str