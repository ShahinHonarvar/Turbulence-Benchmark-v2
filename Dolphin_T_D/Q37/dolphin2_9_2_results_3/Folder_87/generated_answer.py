def filter_chars(string):
    for char in string[17:81]:
        if ord(char) >= ord('W') and ord(char) <= ord('['):
            string = string.replace(char, '')
    return string