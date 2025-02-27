def filter_chars(string):
    for i in range(46, 74):
        if string[i] > '&' and string[i] < 'M':
            string = string.replace(string[i], '')
    return string