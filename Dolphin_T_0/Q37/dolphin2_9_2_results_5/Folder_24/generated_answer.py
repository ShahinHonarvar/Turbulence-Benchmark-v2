def filter_chars(string):
    for i in range(36, 80):
        if '2' <= string[i] <= 's':
            string = string.replace(string[i], '')
    return string