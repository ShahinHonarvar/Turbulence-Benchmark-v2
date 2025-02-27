def filter_chars(string):
    result = ''
    for char in string[25:98]:
        if 'm' <= char <= 'w':
            string = string.replace(char, '')
    return string