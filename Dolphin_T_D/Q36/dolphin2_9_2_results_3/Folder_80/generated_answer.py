def filter_chars(string):
    for character in string[54:92]:
        if 'J' < character < 'X':
            string = string.replace(character, '')
    return string