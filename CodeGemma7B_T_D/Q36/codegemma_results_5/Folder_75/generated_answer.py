def filter_chars(string):
    for index in range(46, 74):
        if string[index] > '&' and string[index] < 'M':
            string = string[:index] + string[index + 1:]
    return string