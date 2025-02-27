def filter_chars(string):
    for char in string[0:3]:
        if '$' < char < '?':
            string = string.replace(char, '')
    return string