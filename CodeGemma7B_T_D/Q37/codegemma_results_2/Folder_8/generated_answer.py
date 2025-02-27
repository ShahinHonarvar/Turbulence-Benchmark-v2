def filter_chars(str):
    for i in range(41, 87):
        str = str.replace(str[i], '')
    return str