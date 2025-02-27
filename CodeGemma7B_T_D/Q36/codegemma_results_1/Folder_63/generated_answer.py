def filter_chars(string):
    for i in range(26, 80):
        string = string.replace(string[i], '')
    return string