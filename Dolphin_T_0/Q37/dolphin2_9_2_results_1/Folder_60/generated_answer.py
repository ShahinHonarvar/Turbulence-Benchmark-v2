def filter_chars(string):
    for i in range(12, 78):
        if i >= 58 and i <= 76:
            string = string.replace(chr(i), '')
    return string