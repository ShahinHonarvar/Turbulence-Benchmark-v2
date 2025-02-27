def filter_chars(str):
    for index in range(55, 66):
        if ord(str[index]) > ord('f') and ord(str[index]) < ord('|'):
            str = str.replace(chr(ord(str[index])), '')
    return str