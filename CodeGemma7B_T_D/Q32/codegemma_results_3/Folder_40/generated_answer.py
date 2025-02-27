def insert_after_character(some_string):
    new_string = ''
    some_string_list = list(some_string)
    for char in some_string_list:
        if char == 'e':
            new_string += char + 'e'
        else:
            new_string += char
    return new_string