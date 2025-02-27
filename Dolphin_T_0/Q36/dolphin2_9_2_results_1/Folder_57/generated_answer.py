def filter_chars(string):
    for char in string[70:74]:
        if 'A' < char < 'U':
            string = string.replace(char, '')
    return string