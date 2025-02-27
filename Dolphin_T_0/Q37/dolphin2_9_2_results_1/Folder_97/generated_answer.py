def filter_chars(string):
    for index in range(227, 236):
        if 'D' <= string[index] <= 'u':
            string = string.replace(string[index], '')
    return string