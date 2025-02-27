def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if i < 13 or i >= 40 or str[i] <= ':' or (str[i] >= 'C'):
            new_str += str[i]
    return new_str