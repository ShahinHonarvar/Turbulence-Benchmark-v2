def filter_chars(string):
    for char in string[72:93]:
        if '<' < char < 'J':
            string = string.replace(char, '')
    return string