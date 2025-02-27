def filter_chars(str):
    for i in range(3, 9):
        if ord(str[i]) > ord('*') and ord(str[i]) < ord('E'):
            str = str.replace(str[i], '')
    return str