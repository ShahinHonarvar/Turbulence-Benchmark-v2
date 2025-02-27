def insert_after_character(str):
    modified_str = ''
    for char in str:
        if char == 'C':
            modified_str += char + 'H'
        else:
            modified_str += char
    return modified_str