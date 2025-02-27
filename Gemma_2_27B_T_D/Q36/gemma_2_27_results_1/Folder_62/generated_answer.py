def filter_chars(string):
    for i in range(63, 89):
        char = chr(i)
        if char > '*' and char < 'w':
            string = string.replace(char, '')
    return string