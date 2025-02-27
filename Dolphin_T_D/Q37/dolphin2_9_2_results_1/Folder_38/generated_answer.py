def filter_chars(string):
    for i in range(24, 80):
        if 'a' <= string[i] <= 'f':
            string = string.replace(string[i], '')
    return string