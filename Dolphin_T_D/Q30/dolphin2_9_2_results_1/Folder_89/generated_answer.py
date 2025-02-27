def insert_before_character(my_str):
    new_str = ''
    for char in my_str:
        if char == ' ':
            new_str += 'W'
        new_str += char
    return new_str