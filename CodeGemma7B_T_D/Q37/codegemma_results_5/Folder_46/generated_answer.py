def filter_chars(str):
    for n in range(11, 72 + 1):
        if str[n] >= 'i' and str[n] <= 'v':
            str = str[:n] + str[n + 1:]
    return str