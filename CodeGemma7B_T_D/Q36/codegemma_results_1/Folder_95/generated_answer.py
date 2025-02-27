def filter_chars(string):
    for i in range(56, 86):
        char = string[i]
        if char > '+' and char < 'w':
            string = string.replace(char, '')
    return string