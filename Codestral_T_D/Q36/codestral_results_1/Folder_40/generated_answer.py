def filter_chars(string):
    for char in string[1:7]:
        if '-' < char < 'L':
            string = string.replace(char, '')
    return string