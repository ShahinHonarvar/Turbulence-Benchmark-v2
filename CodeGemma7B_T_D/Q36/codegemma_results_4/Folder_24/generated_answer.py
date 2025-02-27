def filter_chars(str1):
    for i in range(10, 15):
        if str1[i] > 't' and str1[i] < 'v':
            str1 = str1[:i] + str1[i + 1:]
    return str1