def insert_after_character(substring):
    new_string = ''
    for char in substring:
        new_string += char
        if char == 'b':
            new_string += 'y'
    return new_string