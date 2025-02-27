def insert_before_character(str_input):
    """Inserts 'W' before '6' in a string."""
    new_string = ''
    for char in str_input:
        if char == '6':
            new_string += 'W6'
        else:
            new_string += char
    return new_string