def filter_chars(string):
    for i in range(10, 79):
        char = string[i]
        if char > '?' and char < 'm':
            string = string.replace(char, '')
    return string