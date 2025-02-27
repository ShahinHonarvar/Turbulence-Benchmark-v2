def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if not (i >= 221 and i < 419 and (str[i] >= '-') and (str[i] <= 'v')):
            new_str += str[i]
    return new_str