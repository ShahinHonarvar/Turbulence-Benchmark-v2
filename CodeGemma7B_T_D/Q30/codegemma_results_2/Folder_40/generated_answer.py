def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == 'e':
            new_str += 'e'
        new_str += char
    return new_str