def filter_chars(string):
    for i in range(44, 68):
        char = string[i]
        if char > 'W' and char < 'x':
            string = string.replace(char, '')
    return string