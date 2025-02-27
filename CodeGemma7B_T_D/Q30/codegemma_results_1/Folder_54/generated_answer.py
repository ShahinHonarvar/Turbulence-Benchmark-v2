def insert_before_character(user_input):
    new_string = []
    for character in user_input:
        if character == 'M':
            new_string.append('f')
            new_string.append(character)
        else:
            new_string.append(character)
    return ''.join(new_string)