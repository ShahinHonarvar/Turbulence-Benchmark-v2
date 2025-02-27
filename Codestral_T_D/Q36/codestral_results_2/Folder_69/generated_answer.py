def filter_chars(string):
    for i in range(343, 665):
        char = string[i]
        if '%' < char < 'U':
            string = string.replace(char, '')
    return string