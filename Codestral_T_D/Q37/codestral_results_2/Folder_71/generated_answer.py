def filter_chars(string):
    for i in range(32, 47):
        if '0' <= string[i] <= 'k':
            string = string.replace(string[i], '')
    return string