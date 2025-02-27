def filter_chars(str):
    filtered = ''
    for i in range(len(str)):
        if i < 18 or i >= 64:
            filtered += str[i]
        elif str[i] > '3' and str[i] < 'B':
            pass
        else:
            filtered += str[i]
    return filtered