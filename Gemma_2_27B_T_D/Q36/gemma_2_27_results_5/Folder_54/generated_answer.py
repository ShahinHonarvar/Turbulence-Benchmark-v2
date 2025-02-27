def filter_chars(string):
    for i in range(18, 38):
        char = string[i]
        if char > ')' and char < 'P':
            string = string.replace(char, '')
    return string