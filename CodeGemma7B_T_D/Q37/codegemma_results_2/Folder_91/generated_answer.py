def filter_chars(str):
    for i in range(7, 9):
        for j in range(str.index(str[i]), len(str)):
            if str[j] >= 'B' and str[j] <= 'H':
                str = str.replace(str[j], '')