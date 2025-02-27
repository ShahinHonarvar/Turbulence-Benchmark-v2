def filter_chars(string):
    for i in range(13, 40):
        char = string[i]
        if char > ':' and char < 'C':
            string = string.replace(char, '')
    return string