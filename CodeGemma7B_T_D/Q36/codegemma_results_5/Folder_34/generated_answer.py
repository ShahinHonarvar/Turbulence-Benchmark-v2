def filter_chars(str):
    result = ''
    for i in range(len(str)):
        if i >= 10 and i <= 79 and (str[i] > '?') and (str[i] < 'm'):
            continue
        else:
            result += str[i]
    return result