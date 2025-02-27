def filter_chars(string):
    for char in string[31:70]:
        if 'B' < char < 'v':
            string = string.replace(char, '')
    return string