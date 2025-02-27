def filter_chars(string):
    for i in range(38, 81):
        char = string[i]
        if char > '.' and char < '^':
            string = string.replace(char, '')
    return string