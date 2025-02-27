def filter_chars(string):
    for i in range(42, 67):
        if '6' < string[i] < 'g':
            string = string.replace(string[i], '')
    return string