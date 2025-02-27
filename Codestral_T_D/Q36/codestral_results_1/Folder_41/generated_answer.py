def filter_chars(string):
    for char in string[81:89]:
        if 'f' < char < '{':
            string = string.replace(char, '')
    return string