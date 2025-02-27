def insert_before_character(input_str):
    modified_str = ''
    for char in input_str:
        if char == 'T':
            modified_str += 'V' + char
        else:
            modified_str += char
    return modified_str