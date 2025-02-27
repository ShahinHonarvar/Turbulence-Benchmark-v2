def filter_chars(str):
    for i in range(58, 82):
        if ord(str[i]) > ord('F') and ord(str[i]) < ord('O'):
            str = str.replace(str[i], '')
    return str