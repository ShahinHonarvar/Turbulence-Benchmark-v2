def insert_after_character(string):
    new_string = ''
    for char in string:
        if char == 'o':
            new_string += char + 'h'
        else:
            new_string += char
    return new_string