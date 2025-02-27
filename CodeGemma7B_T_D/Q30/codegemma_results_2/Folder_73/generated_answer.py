def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == 'R':
            new_str += 'V' + char
        else:
            new_str += char
    return new_str