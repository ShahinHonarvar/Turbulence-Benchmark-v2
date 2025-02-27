def filter_chars(str):
    for i in range(373, 902):
        if str[i] >= 'T' and str[i] <= 'h':
            str = str[:i] + str[i + 1:]
    return str