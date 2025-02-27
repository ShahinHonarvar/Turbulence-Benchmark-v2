def filter_chars(string):
    for char in [ch for ch in string[20:80] if '!' <= ch <= 'T']:
        string = string.replace(char, '')
    return string