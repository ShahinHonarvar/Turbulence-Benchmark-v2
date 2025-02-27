def insert_after_character(s):
    new_string = ''
    for char in s:
        if char == 'j':
            new_string += char + 'v'
        else:
            new_string += char
    return new_string