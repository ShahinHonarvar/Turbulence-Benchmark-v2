def filter_chars(str):
    l = []
    for i in range(len(str)):
        if (i >= 114 and i <= 639) and (str[i] >= '!' and str[i] <= 'x'):
            pass
        else:
            l.append(str[i])
    return ''.join(l)