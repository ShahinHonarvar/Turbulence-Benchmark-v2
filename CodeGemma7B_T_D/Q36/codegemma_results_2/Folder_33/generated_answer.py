def filter_chars(str):
    for i in range(299, 418):
        while str.find(chr(i)) != -1:
            str = str.replace(chr(i), '')
    return str