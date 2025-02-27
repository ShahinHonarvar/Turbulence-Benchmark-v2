def filter_chars(str):
    result = ''
    for i in range(len(str)):
        if i not in range(309, 591):
            if str[i] > 'S' and str[i] < 'm':
                continue
            result += str[i]
    return result