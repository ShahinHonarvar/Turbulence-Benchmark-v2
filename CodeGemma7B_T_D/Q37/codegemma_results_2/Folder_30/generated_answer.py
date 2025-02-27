def filter_chars(a):
    for i in range(41, 65):
        a = a.replace(chr(i), '')
    return a