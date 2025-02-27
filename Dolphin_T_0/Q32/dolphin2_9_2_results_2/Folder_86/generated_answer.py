def insert_after_character(s):
    new_string = ''
    for char in s:
        new_string += char
        if char == 'O':
            new_string += 'Q'
    return new_string