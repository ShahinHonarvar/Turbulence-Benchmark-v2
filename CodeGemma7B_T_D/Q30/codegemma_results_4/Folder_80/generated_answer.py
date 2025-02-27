def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == ' ':
            new_str += 'X '
        else:
            new_str += char
    return new_str