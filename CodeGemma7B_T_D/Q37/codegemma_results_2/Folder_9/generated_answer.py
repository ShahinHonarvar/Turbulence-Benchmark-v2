def filter_chars(str):
    for i in range(40, 100):
        str = str.replace(str[i], '')
    return str