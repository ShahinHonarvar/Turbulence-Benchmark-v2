def filter_chars(string):
    for i in range(10, 70):
        if 'I' <= string[i] <= 'K':
            string = string.replace(string[i], '')
    return string