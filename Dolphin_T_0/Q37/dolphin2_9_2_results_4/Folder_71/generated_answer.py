def filter_chars(string):
    for char in string:
        if 32 <= ord(char) <= 46 and '0' <= char <= 'k':
            string = string.replace(char, '')
    return string