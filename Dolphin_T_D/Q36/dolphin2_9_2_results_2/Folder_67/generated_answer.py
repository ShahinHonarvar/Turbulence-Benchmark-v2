def filter_chars(string):
    for char in string[18:31]:
        if 'H' < char < '|':
            string = string.replace(char, '')
    return string