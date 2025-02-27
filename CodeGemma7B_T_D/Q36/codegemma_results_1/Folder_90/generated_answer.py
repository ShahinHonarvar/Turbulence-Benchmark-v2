def filter_chars(str):
    str = list(str)
    for i in range(344, 874):
        if str[i] > 'f' and str[i] < '~':
            for j in range(str.count(str[i])):
                str.remove(str[i])
    str = ''.join(str)
    return str