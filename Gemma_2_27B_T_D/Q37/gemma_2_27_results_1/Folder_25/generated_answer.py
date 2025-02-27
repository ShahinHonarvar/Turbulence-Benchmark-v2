def filter_chars(string):
    for i in range(31, 39):
        char = string[i]
        if char >= ';' and char <= 'g':
            string = string.replace(char, '')
    return string