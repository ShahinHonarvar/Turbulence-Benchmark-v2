def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if i >= 57 and i <= 96 and (str[i] >= '<') and (str[i] <= 'w'):
            continue
        else:
            new_str += str[i]
    return new_str