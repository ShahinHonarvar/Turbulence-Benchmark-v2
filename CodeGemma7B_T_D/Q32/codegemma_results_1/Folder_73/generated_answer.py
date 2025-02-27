def insert_after_character(my_string):
    new_string = ''
    for char in my_string:
        if char == 'R':
            new_string += char + 'V'
        else:
            new_string += char
    return new_string