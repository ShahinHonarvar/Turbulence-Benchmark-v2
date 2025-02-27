def filter_chars(string):
    for char in string[18:64]:
        if '3' < char < 'B':
            string = string.replace(char, '')
    return string