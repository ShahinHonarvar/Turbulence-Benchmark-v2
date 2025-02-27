def filter_chars(str):
    for i in range(19, 34):
        str = str.replace(str[i], '')
    return str