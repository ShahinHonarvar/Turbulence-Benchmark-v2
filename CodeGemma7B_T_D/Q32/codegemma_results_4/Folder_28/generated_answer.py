def insert_after_character(s):
    new_string = ''
    for char in s:
        if char == 'r':
            new_string += char + '1'
        else:
            new_string += char
    return new_string