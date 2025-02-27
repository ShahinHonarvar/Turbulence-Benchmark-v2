def filter_chars(string):
    for char in sorted(set(string[24:80])):
        if 'a' <= char <= 'f':
            string = string.replace(char, '')
    return string