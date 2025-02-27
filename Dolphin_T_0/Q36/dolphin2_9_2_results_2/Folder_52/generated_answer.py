def filter_chars(string):
    for char in string:
        if 49 < string.index(char) < 56 and 'I' < char < 'a':
            string = string.replace(char, '')
    return string