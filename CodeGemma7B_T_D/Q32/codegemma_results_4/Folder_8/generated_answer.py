def insert_after_character(str):
    new_str = ''
    for char in str:
        if char == 'E':
            new_str += 'E' + 'T'
        else:
            new_str += char
    return new_str