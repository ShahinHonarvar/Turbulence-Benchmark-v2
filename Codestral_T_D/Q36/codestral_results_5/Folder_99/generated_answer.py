def filter_chars(string):
    for char in string[476:948]:
        if 'b' < char < 'd':
            string = string.replace(char, '')
    return string