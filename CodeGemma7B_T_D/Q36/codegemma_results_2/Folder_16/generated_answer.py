def filter_chars(str):
    for i in range(331, 713):
        while str.find(chr(i)) != -1:
            str = str.replace(chr(i), '', 1)
    return str