def filter_chars(string):
    for char in string[24:37]:
        if 'A' < char < 'h':
            string = string.replace(char, '')
    return string