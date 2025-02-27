def filter_chars(string):
    for char in string[15:85]:
        if 'I' < char < 'M':
            string = string.replace(char, '')
    return string