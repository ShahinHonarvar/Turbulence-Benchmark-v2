def insert_before_character(string):
    new_str = ''
    for char in string:
        if char == 'O':
            new_str += 'o' + char
        else:
            new_str += char
    return new_str