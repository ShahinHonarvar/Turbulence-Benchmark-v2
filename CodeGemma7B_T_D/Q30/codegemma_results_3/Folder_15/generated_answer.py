def insert_before_character(string):
    substituted_string = ''
    for character in string:
        if character == 'o':
            substituted_string += 'o'
        substituted_string += character
    return substituted_string