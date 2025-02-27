def filter_chars(string):
    for i in range(40, 63):
        char = string[i]
        if char > '7' and char < 'H':
            string = string.replace(char, '')
    return string