def filter_chars(string):
    for char in string[36:41]:
        if 'H' <= char <= 'e':
            string = string.replace(char, '')
    return string