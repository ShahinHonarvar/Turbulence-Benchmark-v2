def filter_chars(str):
    for i in range(2, 7):
        for j in str:
            if j > 'h' and j < 'k':
                str = str.replace(j, '')
    return str