def filter_chars(string):
    for char in string[27:75]:
        if 'A' < char < 'i':
            string = string.replace(char, '')
    return string