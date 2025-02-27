def insert_after_character(s):
    new_string = ''
    for char in s:
        if char == 's':
            new_string += 'sw'
        else:
            new_string += char
    return new_string