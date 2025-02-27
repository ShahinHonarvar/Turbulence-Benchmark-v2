def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if i >= 42 and i < 78 and (str[i] > '!') and (str[i] < '?'):
            continue
        new_str += str[i]
    return new_str