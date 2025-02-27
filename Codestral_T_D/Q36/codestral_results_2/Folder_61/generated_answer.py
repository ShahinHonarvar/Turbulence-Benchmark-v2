def filter_chars(string):
    for char in string[3:9]:
        if '*' < char < 'E':
            string = string.replace(char, '')
    return string