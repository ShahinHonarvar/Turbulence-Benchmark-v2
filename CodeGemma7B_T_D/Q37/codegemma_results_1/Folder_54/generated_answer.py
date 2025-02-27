def filter_chars(string):
    for i in range(46, 85 + 1):
        char = string[i]
        if char >= '-' and char <= 'X':
            string = string.replace(char, '')
    return string