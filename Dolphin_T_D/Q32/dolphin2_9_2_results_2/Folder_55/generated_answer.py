def insert_after_character(s):
    new_string = ''
    for char in s:
        new_string += char
        if char == 'u':
            new_string += 'U'
    return new_string