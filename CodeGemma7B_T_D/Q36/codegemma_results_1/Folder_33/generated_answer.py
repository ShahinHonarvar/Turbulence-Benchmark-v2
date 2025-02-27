def filter_chars(str):
    result = ''
    for i in range(len(str)):
        if i >= 299 and i <= 418:
            if str[i] > '9' and str[i] < 'P':
                continue
        result += str[i]
    return result