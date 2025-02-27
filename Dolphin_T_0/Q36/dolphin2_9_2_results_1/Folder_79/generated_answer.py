def filter_chars(string):
    for i in range(11, 46):
        char = string[i]
        if char > '!' and char < 'A':
            string = string.replace(char, '')
    return string