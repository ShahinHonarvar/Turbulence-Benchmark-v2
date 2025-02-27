def filter_chars(string):
    for i in range(31, 50):
        if string[i] > '/' and string[i] < 'J':
            string = string.replace(string[i], '')
    return string