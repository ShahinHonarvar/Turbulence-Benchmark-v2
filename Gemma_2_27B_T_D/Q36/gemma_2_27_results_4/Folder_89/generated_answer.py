def filter_chars(string):
    for i in range(57, 69):
        char = string[i]
        if char > '(' and char < 'W':
            string = string.replace(char, '')
    return string