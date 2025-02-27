def insert_after_character(string):
    new_string = ''
    for ch in string:
        if ch == 'U':
            new_string += ch + 'F'
        else:
            new_string += ch
    return new_string