def filter_chars(string):
    for i in range(86, 93):
        if string[i] > 'E' and string[i] < '~':
            string = string.replace(string[i], '')
    return string