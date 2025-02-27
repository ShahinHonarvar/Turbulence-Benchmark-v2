def filter_chars(string):
    for i in range(46, 68):
        if string[i] > 'H' and string[i] < 's':
            string = string.replace(string[i], '')
    return string