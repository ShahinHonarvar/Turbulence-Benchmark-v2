def filter_chars(str):
    for i in range(672, 709):
        str = str.replace(chr(i), '')
    return str