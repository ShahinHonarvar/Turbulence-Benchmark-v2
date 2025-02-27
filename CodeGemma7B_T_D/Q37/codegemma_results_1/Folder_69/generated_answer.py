def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if str[i] < '!':
            continue
        if str[i] > 'x':
            continue
        if i >= 114 and i <= 639:
            continue
        new_str += str[i]
    return new_str