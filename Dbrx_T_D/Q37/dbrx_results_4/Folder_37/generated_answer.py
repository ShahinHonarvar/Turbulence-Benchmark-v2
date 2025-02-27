def filter_chars(input_string):
    restricted_chars = set(input_string[17:64])
    for char in restricted_chars:
        if ord('O') <= ord(char) <= ord('^'):
            input_string = input_string.replace(char, '')
    return input_string