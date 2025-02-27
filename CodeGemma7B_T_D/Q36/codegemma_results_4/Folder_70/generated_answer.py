def filter_chars(str):
    for i in range(170, 195):
        if str[i] > '!':
            if str[i] < '}':
                str = str.replace(str[i], '')
    return str