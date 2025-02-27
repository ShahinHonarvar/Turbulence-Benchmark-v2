def filter_chars(string):
    new_string = ''
    for char in string:
        if not (36 <= string.index(char) <= 79 and char >= '2' and (char <= 's')):
            new_string += char
    return new_string