def insert_before_character(string):
    modified_string = ''
    insert_character = 'P'
    for char in string:
        if char == ' ':
            modified_string += insert_character + char
        else:
            modified_string += char
    return modified_string