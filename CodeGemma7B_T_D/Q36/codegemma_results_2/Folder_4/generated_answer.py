def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if i < 42 or i >= 67:
            new_str += str[i]
        elif str[i] > '6' and str[i] < 'g':
            continue
    return new_str