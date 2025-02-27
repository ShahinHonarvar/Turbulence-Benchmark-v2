def insert_after_character(input_string):
    output_string = ''
    insert = False
    for character in input_string:
        if character == 'X':
            insert = True
        if insert:
            output_string += 'u'
            insert = False
        output_string += character
    return output_string