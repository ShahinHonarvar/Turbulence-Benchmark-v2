def insert_before_character(input_str):
    new_str = ''
    for char in input_str:
        if char == 'a':
            new_str += 'W' + char
        else:
            new_str += char
    return new_str