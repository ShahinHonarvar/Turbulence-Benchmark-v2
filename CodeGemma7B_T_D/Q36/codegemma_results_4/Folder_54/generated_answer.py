def filter_chars(str):
    for i in range(18, 38):
        while str[i] > ')' and str[i] < 'P' and (str[i] in str):
            str = str.replace(str[i], '')
    return str