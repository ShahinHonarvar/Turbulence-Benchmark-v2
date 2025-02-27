def filter_chars(string):
    for char in string[44:59]:
        if '/' < char < '6':
            string = string.replace(char, '')
    return string