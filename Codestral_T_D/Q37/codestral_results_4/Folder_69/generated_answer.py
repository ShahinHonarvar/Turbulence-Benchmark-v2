def filter_chars(string):
    for char in string[114:640]:
        if '!' <= char <= 'x':
            string = string.replace(char, '')
    return string