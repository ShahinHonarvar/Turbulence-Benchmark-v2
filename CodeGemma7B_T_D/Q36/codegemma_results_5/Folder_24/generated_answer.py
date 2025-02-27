def filter_chars(str):
    s = ''
    for i in range(len(str)):
        if i not in range(10, 15):
            if str[i] > 't' and str[i] < 'v':
                continue
            s += str[i]
    return s