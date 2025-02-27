def filter_chars(string):
    for char in string[43:69]:
        if 'B' < char < 'r':
            string = string.replace(char, '')
    return string