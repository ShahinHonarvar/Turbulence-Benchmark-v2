def insert_after_character(input_str):
    new_str = ''
    for char in input_str:
        if char == 'i':
            new_str += char + 'I'
        else:
            new_str += char
    return new_str