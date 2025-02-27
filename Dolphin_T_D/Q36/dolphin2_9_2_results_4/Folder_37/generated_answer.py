def filter_chars(string):
    for i in range(44, 59):
        if string[i] > '/' and string[i] < '6':
            string = string.replace(string[i], '')
    return string