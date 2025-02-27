def filter_chars(string):
    for char in string[31:70]:
        if char > 'B' and char < 'v':
            string = string.replace(char, '')
    return string