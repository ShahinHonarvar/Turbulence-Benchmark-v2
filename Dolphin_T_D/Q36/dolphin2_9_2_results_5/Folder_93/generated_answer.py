def filter_chars(string):
    for character in range(52, 88):
        if string[character] > '&' and string[character] < 'c':
            string = string.replace(string[character], '')
    return string