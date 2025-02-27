def filter_chars(string):
    for i in range(44, 48):
        char = string[i]
        if char > '+' and char < 'l':
            string = string.replace(char, '')
    return string