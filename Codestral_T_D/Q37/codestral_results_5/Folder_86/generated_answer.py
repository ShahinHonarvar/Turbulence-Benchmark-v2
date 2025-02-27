def filter_chars(string):
    for char in string[164:707]:
        if 'O' <= char <= '}':
            string = string.replace(char, '')
    return string