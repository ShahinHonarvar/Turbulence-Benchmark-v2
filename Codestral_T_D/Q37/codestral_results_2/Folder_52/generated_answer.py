def filter_chars(string):
    for char in string[54:84]:
        if 'j' <= char <= 'v':
            string = string.replace(char, '')
    return string