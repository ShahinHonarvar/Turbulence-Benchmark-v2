def filter_chars(string):
    for char in string[283:484]:
        if 'l' < char < 't':
            string = string.replace(char, '')
    return string