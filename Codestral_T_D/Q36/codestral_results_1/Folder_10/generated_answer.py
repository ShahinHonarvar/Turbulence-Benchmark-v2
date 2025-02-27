def filter_chars(string):
    for char in string[35:60]:
        if '!' < char < 'B':
            string = string.replace(char, '')
    return string