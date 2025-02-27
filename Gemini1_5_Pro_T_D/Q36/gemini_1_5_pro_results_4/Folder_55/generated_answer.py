def filter_chars(string):
    for i in range(3, 5):
        if i < len(string) and 'Y' < string[i] < 's':
            string = string.replace(string[i], '')
    return string