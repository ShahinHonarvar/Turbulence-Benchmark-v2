def filter_chars(string):
    for character in string:
        if 'f' < character < '|':
            string = string.replace(character, '')
    return string