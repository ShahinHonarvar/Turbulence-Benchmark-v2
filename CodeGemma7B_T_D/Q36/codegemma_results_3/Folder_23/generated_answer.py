def filter_chars(str):
    for i in range(21, 25):
        if ord(str[i]) > ord('5') and ord(str[i]) < ord('}'):
            str = str.replace(str[i], '')
    return str