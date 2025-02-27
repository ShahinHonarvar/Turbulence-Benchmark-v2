def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == 'a':
            new_str += 'A' + char
        else:
            new_str += char
    return new_str