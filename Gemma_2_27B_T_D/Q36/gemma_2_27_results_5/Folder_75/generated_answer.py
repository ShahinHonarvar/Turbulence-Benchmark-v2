def filter_chars(string):
    for i in range(46, 74):
        char = string[i]
        if char > '&' and char < 'M':
            string = string.replace(char, '')
    return string