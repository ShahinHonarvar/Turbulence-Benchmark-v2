def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == 'r':
            new_str += 'w' + char
        else:
            new_str += char
    return new_str