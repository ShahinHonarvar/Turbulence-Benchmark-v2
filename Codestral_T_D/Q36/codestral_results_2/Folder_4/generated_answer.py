def filter_chars(string):
    for char in string[42:67]:
        if '6' < char < 'g':
            string = string.replace(char, '')
    return string