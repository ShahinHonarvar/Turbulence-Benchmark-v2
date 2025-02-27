def insert_after_character(input_string):
    new_string = ''
    for ch in input_string:
        new_string += ch
        if ch == 'E':
            new_string += 'f'
    return new_string