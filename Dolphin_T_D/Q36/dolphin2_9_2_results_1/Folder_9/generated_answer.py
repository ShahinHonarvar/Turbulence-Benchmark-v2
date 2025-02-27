def filter_chars(string):
    for i in range(50, 92):
        char = string[i]
        if 'A' < char < 'Q':
            string = string.replace(char, '')
    return string