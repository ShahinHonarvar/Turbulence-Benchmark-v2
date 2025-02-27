def filter_chars(str):
    for i in range(78, 81):
        if ord(str[i]) > ord('S') and ord(str[i]) < ord('['):
            str = str.replace(str[i], '')
    return str