def filter_chars(str):
    for i in range(165, 707):
        if ord(str[i]) >= ord('O') and ord(str[i]) <= ord('}'):
            str = str.replace(str[i], '')
    return str