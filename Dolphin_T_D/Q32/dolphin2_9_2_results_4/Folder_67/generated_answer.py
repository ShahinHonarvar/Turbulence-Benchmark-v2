def insert_after_character(s):
    new_string = ''
    for char in s:
        new_string += char
        if char == 'j':
            new_string += '1'
    return new_string