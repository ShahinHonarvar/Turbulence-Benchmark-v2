def insert_before_character(s):
    new_string = ''
    for char in s:
        new_string += char
        if char == ' ':
            new_string += 'X'
    return new_string