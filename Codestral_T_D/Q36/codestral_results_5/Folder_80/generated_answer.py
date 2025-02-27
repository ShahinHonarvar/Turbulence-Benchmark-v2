def filter_chars(string):
    for char in string[54:92]:
        if 'J' < char < 'X':
            string = string.replace(char, '')
    return string