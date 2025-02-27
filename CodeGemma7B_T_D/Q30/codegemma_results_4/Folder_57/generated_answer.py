def insert_before_character(string):
    modified_string = ''
    for char in string:
        if char == 's':
            modified_string += 'w' + char
        else:
            modified_string += char
    return modified_string