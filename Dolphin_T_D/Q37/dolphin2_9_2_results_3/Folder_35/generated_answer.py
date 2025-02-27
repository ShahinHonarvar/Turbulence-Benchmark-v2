def filter_chars(string):
    for char in string:
        if 155 <= string.index(char) <= 403 and '(' <= char <= ']':
            string = string.replace(char, '')
    return string