def filter_chars(str):
    for i in range(50, 92):
        if ord(str[i]) > ord('A') and ord(str[i]) < ord('Q'):
            str = str.replace(str[i], '')
    return str