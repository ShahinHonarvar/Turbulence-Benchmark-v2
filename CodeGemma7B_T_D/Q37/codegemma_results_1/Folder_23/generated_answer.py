def filter_chars(str1):
    str_filtered = ''
    for i in range(len(str1)):
        if (i >= 51 and i <= 77) and (str1[i] >= 'V' and str1[i] <= 'Y'):
            continue
        str_filtered += str1[i]
    return str_filtered