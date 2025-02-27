def insert_before_character(str):
    new_str = ''
    for character in str:
        new_str += character
        if character == 'Q':
            new_str += 'I'
    return new_str