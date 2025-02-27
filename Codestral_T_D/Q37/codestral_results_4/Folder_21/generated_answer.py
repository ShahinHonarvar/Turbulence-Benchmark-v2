def filter_chars(string):
    for char in string[603:760]:
        if 'Q' <= char <= 'h':
            string = string.replace(char, '')
    return string