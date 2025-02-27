def filter_chars(str1):
    new_str = ''
    for i in range(len(str1)):
        if i >= 502 and i < 946 and (str1[i] > 'W') and (str1[i] < 'y'):
            continue
        new_str += str1[i]
    return new_str