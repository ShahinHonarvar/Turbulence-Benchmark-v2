def filter_chars(string):
    for char in string[221:419]:
        if '-' < char < 'v':
            string = string.replace(char, '')
    return string