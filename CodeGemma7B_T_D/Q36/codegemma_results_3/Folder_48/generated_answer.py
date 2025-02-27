def filter_chars(str):
    new_str = ''
    for i in range(len(str)):
        if i < 154 or i >= 222 or (str[i] > 'A' and str[i] < 'f'):
            new_str += str[i]
    return new_str