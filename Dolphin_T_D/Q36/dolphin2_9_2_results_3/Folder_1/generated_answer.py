def filter_chars(string):
    for i in range(69, 87):
        char = string[i]
        if char > '#' and char < 'L':
            string = string.replace(char, '')
    return string