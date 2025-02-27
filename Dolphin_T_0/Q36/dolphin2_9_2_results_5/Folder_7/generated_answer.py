def filter_chars(string):
    for char in string[502:946]:
        if 'W' < char < 'y':
            string = string.replace(char, '')
    return string