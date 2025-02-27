def filter_chars(str):
    for i in range(155, 404):
        if str[i] >= '(' and str[i] <= ']':
            str = str.replace(str[i], '')
    return str