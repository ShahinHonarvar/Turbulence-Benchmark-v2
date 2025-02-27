def filter_chars(string):
    for char in string[1:8]:
        if 'L' <= char <= 'a':
            string = string.replace(char, '')
    return string