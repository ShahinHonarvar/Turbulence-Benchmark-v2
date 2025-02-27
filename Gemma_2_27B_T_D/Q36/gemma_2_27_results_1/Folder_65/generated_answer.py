def filter_chars(string):
    for i in range(58, 82):
        char = string[i]
        if char > 'F' and char < 'O':
            string = string.replace(char, '')
    return string