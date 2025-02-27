def filter_chars(string):
    for i in range(13, 29):
        if 'c' <= string[i] <= 'n':
            string = string.replace(string[i], '')
    return string