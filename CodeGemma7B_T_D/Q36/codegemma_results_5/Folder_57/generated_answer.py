def filter_chars(str):
    for i in range(71, 74):
        c = str[i]
        if 'A' < c and c < 'U':
            str = str.replace(c, '')
    return str