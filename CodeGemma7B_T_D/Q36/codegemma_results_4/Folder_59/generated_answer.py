def filter_chars(str):
    for i in range(3, 8):
        c = str[i]
        if c > '?' and c < 'k':
            str = str.replace(c, '')
    return str