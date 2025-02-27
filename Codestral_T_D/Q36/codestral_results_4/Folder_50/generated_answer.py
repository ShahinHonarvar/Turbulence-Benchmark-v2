def filter_chars(string):
    for i in range(61, 88):
        char = string[i]
        if '%' < char < 'q':
            string = string.replace(char, '')
    return string