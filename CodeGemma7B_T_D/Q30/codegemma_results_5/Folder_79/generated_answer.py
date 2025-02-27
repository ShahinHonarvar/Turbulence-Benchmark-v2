def insert_before_character(string):
    new_string = ''
    for ch in string:
        if ch == 'E':
            new_string += 'E'
        new_string += ch
    return new_string