def filter_chars(str1):
    for i in range(38, 69 + 1):
        if ord(str1[i]) >= ord('H') and ord(str1[i]) <= ord('e'):
            str1 = str1[:i] + str1[i + 1:]
    return str1