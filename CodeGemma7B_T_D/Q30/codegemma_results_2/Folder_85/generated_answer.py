def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == 'o':
            new_str += 'a' + char
        else:
            new_str += char
    return new_str