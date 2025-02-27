def filter_chars(string):
    for i in range(2, 7):
        if len(string) > i and string[i] >= '?' and (string[i] <= 'f'):
            string = string.replace(string[i], '')
    return string