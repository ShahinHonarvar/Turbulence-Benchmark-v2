def insert_before_character(string):
    new_string = ''
    for char in string:
        new_string += 'H' + char if char == ' ' else char
    return new_string