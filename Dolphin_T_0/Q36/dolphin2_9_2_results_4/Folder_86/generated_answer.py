def filter_chars(string):
    for char in string[672:709]:
        if 'X' < char < '}':
            string = string.replace(char, '')
    return string