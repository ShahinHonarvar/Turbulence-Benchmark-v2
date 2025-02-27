def filter_chars(string):
    for char in string:
        if 164 <= string.index(char) <= 706 and 'O' <= char <= '}':
            string = string.replace(char, '')
    return string