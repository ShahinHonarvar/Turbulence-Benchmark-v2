def filter_chars(string):
    for char in string[44:68]:
        if char > 'W' and char < 'x':
            string = string.replace(char, '')
    return string