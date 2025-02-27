def filter_chars(str):
    for idx in range(48, 75):
        str = str.replace(chr(idx), '')
    return str