def insert_after_character(string):
    new_string = []
    for character in string:
        if character == 'E':
            new_string.append(character)
            new_string.append('T')
        else:
            new_string.append(character)
    return ''.join(new_string)