def filter_chars(string):
    for char in string[20:63]:
        if 'i' <= char <= 'k':
            string = string.replace(char, '')
    return string