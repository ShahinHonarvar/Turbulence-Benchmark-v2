def filter_chars(string):
    for char in string:
        if char >= '@' and char <= 'T' and (string.index(char) in range(10, 53)):
            while char in string:
                string = string.replace(char, '')
    return string