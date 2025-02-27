def insert_after_character(str):
    new_str = ''
    for char in str:
        if char == 'U':
            new_str += char
            new_str += 'U'
            continue
        new_str += char
    return new_str