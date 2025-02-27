def filter_chars(string):
    for char in string[1:9]:
        if '8' < char < 'm':
            string = string.replace(char, '')
    return string