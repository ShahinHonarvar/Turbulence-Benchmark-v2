def filter_chars(string):
    for char in string[14:75]:
        if '9' < char < 'K':
            string = string.replace(char, '')
    return string