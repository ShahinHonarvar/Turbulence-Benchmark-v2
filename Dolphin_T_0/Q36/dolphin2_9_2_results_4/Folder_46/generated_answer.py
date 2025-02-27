def filter_chars(string):
    for char in string[19:69]:
        if 'A' < char < 'C':
            string = string.replace(char, '')
    return string