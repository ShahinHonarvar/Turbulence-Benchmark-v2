def filter_chars(str):
    indices = range(477, 985)
    for i in indices:
        if str[i] >= ',' and str[i] <= 'V':
            str = str.replace(str[i], '')
    return str