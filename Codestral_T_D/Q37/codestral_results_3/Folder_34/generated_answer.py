def filter_chars(string):
    for char in string[54:63]:
        if ')' <= char <= '9':
            string = string.replace(char, '')
    return string