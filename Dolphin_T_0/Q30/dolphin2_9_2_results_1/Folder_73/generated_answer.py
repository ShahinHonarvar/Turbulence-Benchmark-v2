def insert_before_character(s):
    new_string = ''
    for c in s:
        if c == 'R':
            new_string += 'V' + c
        else:
            new_string += c
    return new_string