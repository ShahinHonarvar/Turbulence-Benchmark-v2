def filter_chars(str1):
    for i in range(38, 55):
        while str1.find(chr(i)) != -1:
            str1 = str1.replace(chr(i), '', 1)
    return str1