def insert_after_character(input_str):
    new_str = ''
    for char in input_str:
        new_str += char
        if char == 'F':
            new_str += 'u'
    return new_str