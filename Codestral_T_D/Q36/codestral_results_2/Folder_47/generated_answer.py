def filter_chars(string):
    for char in string[45:57]:
        if 'F' < char < 'n':
            string = string.replace(char, '')
    return string