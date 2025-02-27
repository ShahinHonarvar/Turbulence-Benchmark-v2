def filter_chars(string):
    for char in string[3:5]:
        if char > 'Y' and char < 's':
            string = string.replace(char, '')
    return string