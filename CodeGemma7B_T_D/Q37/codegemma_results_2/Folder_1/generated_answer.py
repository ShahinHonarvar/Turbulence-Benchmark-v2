def filter_chars(str1):
    str2 = ''
    for i in range(len(str1)):
        if i >= 41 and i <= 79 and (str1[i] >= 'f' and str1[i] <= '|'):
            continue
        str2 = str2 + str1[i]
    return str2