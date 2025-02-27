def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == ' ':
            new_str = new_str + 'o'
        new_str = new_str + char
    return new_str