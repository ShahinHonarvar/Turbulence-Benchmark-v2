def filter_chars(string):
    for char in string[421:854]:
        if 'D' < char < 'J':
            string = string.replace(char, '')
    return string