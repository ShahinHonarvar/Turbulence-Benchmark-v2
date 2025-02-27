def filter_chars(str):
    for i in range(77, 87):
        if chr(i) > ';' and chr(i) < 'r':
            str = str.replace(chr(i), '')
    return str