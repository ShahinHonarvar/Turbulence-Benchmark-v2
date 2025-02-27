def filter_chars(string):
    for char in string[309:591]:
        if 'S' < char < 'm':
            string = string.replace(char, '')
    return string