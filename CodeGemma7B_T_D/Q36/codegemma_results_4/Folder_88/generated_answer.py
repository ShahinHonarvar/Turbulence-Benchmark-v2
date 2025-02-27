def filter_chars(str1):
    str2 = ''
    for i in range(len(str1)):
        if i >= 78 and i <= 81:
            if not (str1[i] > 'S' and str1[i] < '['):
                str2 += str1[i]
        else:
            str2 += str1[i]
    return str2