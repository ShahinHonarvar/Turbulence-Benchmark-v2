def filter_chars(str1):
    new_str1 = ''
    for i in range(len(str1)):
        if i >= 3 and i < 9 and (str1[i] > '*') and (str1[i] < 'E'):
            str1 = str1.replace(str1[i], '')
        new_str1 += str1[i]
    return new_str1