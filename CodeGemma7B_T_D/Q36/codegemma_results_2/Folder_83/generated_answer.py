def filter_chars(str):
    for i in range(72, 93):
        x = str[i]
        if x > '<' and x < 'J':
            str = str.replace(x, '')
    return str