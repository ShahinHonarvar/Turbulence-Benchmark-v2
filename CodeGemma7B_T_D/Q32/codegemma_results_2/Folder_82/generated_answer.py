def insert_after_character(str_var):
    new_string = ''
    for char in str_var:
        if char == 'I':
            new_string += char + 'I'
        else:
            new_string += char
    return new_string