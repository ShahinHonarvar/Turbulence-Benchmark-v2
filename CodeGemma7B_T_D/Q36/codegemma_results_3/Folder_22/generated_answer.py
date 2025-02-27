def filter_chars(string):
    for i in range(55, 84):
        char = string[i]
        if ';' < char < 'z':
            while char in string:
                string = string.replace(char, '', 1)
    return string