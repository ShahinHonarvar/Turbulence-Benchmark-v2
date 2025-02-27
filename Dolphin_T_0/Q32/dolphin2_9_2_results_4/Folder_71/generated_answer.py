def insert_after_character(string):
    new_string = ''
    for index, char in enumerate(string):
        if char == '2':
            new_string += char + 'S'
        else:
            new_string += char
    return new_string