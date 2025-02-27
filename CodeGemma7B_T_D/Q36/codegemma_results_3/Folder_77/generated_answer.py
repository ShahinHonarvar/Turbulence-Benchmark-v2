def filter_chars(str):
    for i in range(221, 419):
        while str.count(chr(i)) > 0:
            str = str.replace(chr(i), '')
    return str