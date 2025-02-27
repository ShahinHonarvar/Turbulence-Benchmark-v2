def insert_before_character(my_string):
    new_string = ''
    for char in my_string:
        if char == 'o':
            new_string += 'a' + char
        else:
            new_string += char
    return new_string