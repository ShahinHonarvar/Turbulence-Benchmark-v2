def insert_after_character(str):
    current_position = 0
    new_str = ''
    for character in str:
        new_str += character
        if character == 'U':
            new_str += 'u'
        current_position += 1
    return new_str