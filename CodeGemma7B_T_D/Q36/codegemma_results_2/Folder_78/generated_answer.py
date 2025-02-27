def filter_chars(str):
    result = ''
    for i in range(len(str)):
        if i >= 29 and i <= 33 and (str[i] > '%') and (str[i] < 'a'):
            continue
        result += str[i]
    return result