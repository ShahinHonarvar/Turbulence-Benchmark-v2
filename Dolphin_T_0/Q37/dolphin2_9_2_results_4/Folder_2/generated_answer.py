def filter_chars(string):
    for char in string[477:985]:
        if char >= ',' and char <= 'V':
            string = string.replace(char, '')
    return string