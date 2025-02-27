def insert_after_character(my_str):
    new_str = ''
    for char in my_str:
        new_str += char + ('o' if char == ' ' else '')
    return new_str