def filter_chars(string):
    for i in range(40, 63):
        if i >= len(string):
            break
        char = string[i]
        if '7' < char < 'H':
            string = string.replace(char, '')
    return string