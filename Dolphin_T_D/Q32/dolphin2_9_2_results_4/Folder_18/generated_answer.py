def insert_after_character(string):
    output_string = ''
    for char in string:
        output_string += char
        if char == 'K':
            output_string += 'l'
    return output_string