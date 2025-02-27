def filter_chars(string):
    for char in string[2:7]:
        if 'h' < char < 'k':
            string = string.replace(char, '')
    return string