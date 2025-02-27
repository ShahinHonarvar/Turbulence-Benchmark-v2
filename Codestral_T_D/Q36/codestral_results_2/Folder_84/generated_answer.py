def filter_chars(string):
    for char in string[171:636]:
        if 'c' < char < 's':
            string = string.replace(char, '')
    return string