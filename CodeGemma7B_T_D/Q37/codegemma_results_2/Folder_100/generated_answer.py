def filter_chars(str):
    for i in range(88, 91):
        str = str.replace(chr(i), '')
    return str