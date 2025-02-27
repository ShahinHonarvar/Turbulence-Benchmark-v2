def filter_chars(string):
    for i in range(669, 888):
        char = string[i]
        if 'B' < char < 'Y':
            string = string.replace(char, '')
    return string