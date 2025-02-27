def filter_chars(str):
    result = ''
    for i in range(len(str)):
        if i < 13 or i > 28 or str[i] < 'c' or (str[i] > 'n'):
            result += str[i]
    return result