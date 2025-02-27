def insert_before_character(user_string):
    new_string = ''
    for character in user_string:
        if character == 't':
            new_string += 'u'
        new_string += character
    return new_string