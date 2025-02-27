def filter_chars(string):
    for i in range(63, 89):
        for char in string:
            if char > '*' and char < 'w':
                string = string.replace(char, '')
    return string