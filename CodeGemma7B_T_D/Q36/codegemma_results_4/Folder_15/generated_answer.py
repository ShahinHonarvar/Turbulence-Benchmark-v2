def filter_chars(str):
    for i in range(2, 7):
        c = str[i]
        if c > 'h' and c < 'k':
            str = str.replace(c, '')
    return str