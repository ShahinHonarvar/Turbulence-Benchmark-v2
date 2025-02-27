def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'X':
            new_string += char + '6'
        else:
            new_string += char
    return new_string