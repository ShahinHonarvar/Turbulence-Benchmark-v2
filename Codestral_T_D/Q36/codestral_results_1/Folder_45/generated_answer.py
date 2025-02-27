def filter_chars(string):
    for char in string[81:86]:
        if '!' < char < 's':
            string = string.replace(char, '')
    return string