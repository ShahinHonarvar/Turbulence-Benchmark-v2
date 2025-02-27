def insert_after_character(string):
    modified_string = ''
    for char in string:
        if char == 'O':
            modified_string += char + 'o'
        else:
            modified_string += char
    return modified_string