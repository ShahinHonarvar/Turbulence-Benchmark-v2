def filter_chars(string):
    for i in range(38, 70):
        char = string[i]
        if 'H' <= char <= 'e':
            string = string.replace(char, '')
    return string