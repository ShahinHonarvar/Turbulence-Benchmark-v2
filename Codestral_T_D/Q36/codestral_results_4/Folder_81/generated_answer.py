def filter_chars(string):
    for char in string[51:76]:
        if '5' < char < 'f':
            string = string.replace(char, '')
    return string