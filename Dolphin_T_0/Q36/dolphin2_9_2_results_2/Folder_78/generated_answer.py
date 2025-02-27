def filter_chars(string):
    for char in string[29:33]:
        if char > '%' and char < 'a':
            string = string.replace(char, '')
    return string