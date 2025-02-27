def insert_after_character(input_str):
    new_str = ''
    for char in input_str:
        new_str += char
        if char == 's':
            new_str += 'w'
    return new_str