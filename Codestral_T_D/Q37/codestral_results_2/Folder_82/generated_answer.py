def filter_chars(string):
    filtered_string = ''
    for char in string[12:26]:
        if 'P' <= char <= 'x':
            string = string.replace(char, '')
    return string