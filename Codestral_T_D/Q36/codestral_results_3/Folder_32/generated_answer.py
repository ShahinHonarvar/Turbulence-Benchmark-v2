def filter_chars(string):
    for char in string[40:63]:
        if '7' < char < 'H':
            string = string.replace(char, '')
    return string