def insert_after_character(s):
    new_string = ''
    for c in s:
        new_string += c
        if c == 'U':
            new_string += 'U'
    return new_string