def filter_chars(string):
    for char in string[43:59]:
        if '5' < char < 'C':
            string = string.replace(char, '')
    return string