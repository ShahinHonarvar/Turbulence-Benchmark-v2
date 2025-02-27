def insert_after_character(string):
    stringAddZ = ''
    for char in string:
        if char == 'N':
            stringAddZ = stringAddZ + 'N' + 'z'
        else:
            stringAddZ = stringAddZ + char
    return stringAddZ