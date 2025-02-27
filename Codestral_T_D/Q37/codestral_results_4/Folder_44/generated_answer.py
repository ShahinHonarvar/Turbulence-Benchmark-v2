def filter_chars(string):
    for char in string[21:44]:
        if '+' <= char <= '8':
            string = string.replace(char, '')
    return string