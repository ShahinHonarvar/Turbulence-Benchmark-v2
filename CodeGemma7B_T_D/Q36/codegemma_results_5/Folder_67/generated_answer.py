def filter_chars(str):
    str = list(str)
    for i in range(18, 31):
        if ord(str[i]) > ord('H') and ord(str[i]) < ord('|'):
            str[i] = ''
    str = ''.join(str)
    return str