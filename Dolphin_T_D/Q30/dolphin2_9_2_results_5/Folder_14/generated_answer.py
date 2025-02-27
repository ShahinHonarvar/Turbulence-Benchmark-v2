def insert_before_character(input_str):
    new_str = ''
    for char in input_str:
        if char == 'A':
            new_str += ' ' + char
        else:
            new_str += char
    return new_str