def filter_chars(string):
    for i in range(52, 88):
        if string[i] > '&' and string[i] < 'c':
            while string[i] in string:
                string = string.replace(string[i], '')
    return string