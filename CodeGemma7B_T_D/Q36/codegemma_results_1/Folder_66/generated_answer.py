def filter_chars(a):
    for i in range(39, 87):
        a = a.replace(chr(i), '')
    return a