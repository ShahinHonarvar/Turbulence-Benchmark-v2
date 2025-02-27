def filter_chars(string):
    for i in range(61, 88):
        if chr(i) > '%' and chr(i) < 'q':
            string = string.replace(chr(i), '')
    return string