def filter_chars(string):
    for char in string[46:91]:
        if 'D' < char < 'H':
            string = string.replace(char, '')
    return string