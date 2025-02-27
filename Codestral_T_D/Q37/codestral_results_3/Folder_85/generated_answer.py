def filter_chars(string):
    filtered_string = ''
    for char in string[28:66]:
        if 'O' <= char <= 'd':
            string = string.replace(char, '')
    return string