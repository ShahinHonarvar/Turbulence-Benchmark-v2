def filter_chars(str):
    for i in range(7, 10):
        for l in str:
            if l == str[i] and (l >= '6' and l <= 'w'):
                str = str.replace(l, '')
    return str