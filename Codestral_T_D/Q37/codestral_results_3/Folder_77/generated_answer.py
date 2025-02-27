def filter_chars(string):
    for char in string[384:412]:
        if '/' <= char <= '8':
            string = string.replace(char, '')
    return string