def filter_chars(string):
    for char in string[90:97]:
        if 'j' < char < 'w':
            string = string.replace(char, '')
    return string