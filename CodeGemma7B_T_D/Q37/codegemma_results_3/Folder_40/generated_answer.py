def filter_chars(str):
    result = ''
    for i in range(len(str)):
        if i < 2 and str[i] >= '*' and (str[i] <= 's'):
            continue
        result += str[i]
    return result