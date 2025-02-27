def insert_after_character(s):
    new_string = ''
    for c in s:
        new_string += c
        if c == ' ':
            new_string += 'P'
    return new_string