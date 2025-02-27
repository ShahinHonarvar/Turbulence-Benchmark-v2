def filter_chars(string):
    chars = []
    for char in string:
        if 1 <= string.index(char) <= 5 and '$' <= char <= ';':
            chars.append(char)
    for char in chars:
        string = string.replace(char, '')
    return string