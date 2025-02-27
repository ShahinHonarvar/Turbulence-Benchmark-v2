def insert_before_character(my_str):
    new_str = ''
    for char in my_str:
        if char == 'C':
            new_str += 'Z'
        new_str += char
    return new_str