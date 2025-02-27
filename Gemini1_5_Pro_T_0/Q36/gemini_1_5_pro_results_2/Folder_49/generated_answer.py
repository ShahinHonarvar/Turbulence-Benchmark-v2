def filter_chars(string):
    for i in range(46, 91):
        char = chr(i)
        if char > 'D' and char < 'H':
            string = string.replace(char, '')
    return string