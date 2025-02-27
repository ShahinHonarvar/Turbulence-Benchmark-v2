def insert_before_character(str):
    new_str = ''
    for char in str:
        if char == 'I':
            new_str += 'i' + char
        else:
            new_str += char
    return new_str