def filter_chars(string):
    for c in range(323, 526):
        char = string[c]
        if ')' < char < 'O':
            string = string.replace(char, '')
    return string