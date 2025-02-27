def filter_chars(str):
    for i in range(1, 7):
        ch = str[i]
        if ord(ch) > ord('-') and ord(ch) < ord('L'):
            str = str.replace(ch, '')
    return str