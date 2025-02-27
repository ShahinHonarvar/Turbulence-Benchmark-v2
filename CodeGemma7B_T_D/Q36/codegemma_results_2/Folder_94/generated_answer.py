def filter_chars(str_1):
    for i in range(15, 85):
        if str_1[i] > 'I' and str_1[i] < 'M':
            while True:
                try:
                    idx = str_1.index(str_1[i])
                    str_1 = str_1[:idx] + str_1[idx + 1:]
                except ValueError:
                    break
    return str_1