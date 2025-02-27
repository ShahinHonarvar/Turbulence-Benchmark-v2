def insert_after_character(my_string):
    new_string = ''
    for char in my_string:
        new_string += char
        if char == 'u':
            new_string += 'U'
    return new_string