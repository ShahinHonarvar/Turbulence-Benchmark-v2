def insert_after_character(string):
    new_str = ''
    for char in string:
        if char == 'N':
            new_str += char + 'j'
        else:
            new_str += char
    return new_str