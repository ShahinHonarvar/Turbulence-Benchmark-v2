def filter_chars(string):
    for char in string[39:87]:
        if '!' < char < '}':
            string = string.replace(char, '')
    return string