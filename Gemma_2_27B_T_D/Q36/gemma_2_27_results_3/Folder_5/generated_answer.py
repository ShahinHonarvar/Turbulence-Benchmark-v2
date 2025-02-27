def filter_chars(string):
    for i in range(55, 66):
        char = string[i]
        if 'f' < char < '|':
            string = string.replace(char, '')
    return string