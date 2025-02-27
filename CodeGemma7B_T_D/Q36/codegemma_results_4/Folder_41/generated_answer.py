def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if i < 81 or i > 89 or (str[i] < 'f' or str[i] >= '{'):
            new_str += str[i]
    return new_str