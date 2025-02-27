def filter_chars(string):
    for i in range(171, 636):
        char = string[i]
        if char > 'c' and char < 's':
            string = string.replace(char, '')
    return string