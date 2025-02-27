def insert_before_character(string):
    new_string = []
    for character in string:
        if character == 'a':
            new_string.append('a')
        new_string.append(character)
    return ''.join(new_string)