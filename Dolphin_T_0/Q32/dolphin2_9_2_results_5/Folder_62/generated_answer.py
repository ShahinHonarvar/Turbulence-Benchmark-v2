def insert_after_character(my_string):
    new_string = ''
    for char in my_string:
        new_string += char
        if char == ' ':
            new_string += 'o'
    return new_string