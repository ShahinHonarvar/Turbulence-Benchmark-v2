def filter_chars(string):
    for char in string[61:88]:
        if '%' < char < 'q':
            string = string.replace(char, '')
    return string