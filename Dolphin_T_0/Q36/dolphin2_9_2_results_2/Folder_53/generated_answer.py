def filter_chars(string):
    for char in string:
        if ord('j') < ord(char) < ord('w'):
            string = string.replace(char, '')
    return string