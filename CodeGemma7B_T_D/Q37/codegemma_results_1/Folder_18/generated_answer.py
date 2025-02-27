def filter_chars(str):
    for i in range(770, 971):
        str = str.replace(chr(i), '')
    return str