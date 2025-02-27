def insert_before_character(argument):
    output = ''
    for character in argument:
        if character == 'a':
            output += 'n'
        output += character
    return output