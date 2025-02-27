def filter_chars(string):
    for char in string:
        if 1 <= string.index(char) <= 5 and '$' <= char <= ';':
            string = string.replace(char, '')
    return string