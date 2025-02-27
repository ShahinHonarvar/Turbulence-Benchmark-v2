def filter_chars(string):
    for char in string[318:337]:
        if 'B' < char < 'z':
            string = string.replace(char, '')
    return string