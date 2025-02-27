def filter_chars(string):
    for i in range(90, 97):
        char = string[i]
        if 'j' < char < 'w':
            string = string.replace(char, '')
    return string