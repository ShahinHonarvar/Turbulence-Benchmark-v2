def filter_chars(str):
    res = ''
    for i in range(len(str)):
        if not (str[i] >= ';' and str[i] <= 'g'):
            res += str[i]
    return res