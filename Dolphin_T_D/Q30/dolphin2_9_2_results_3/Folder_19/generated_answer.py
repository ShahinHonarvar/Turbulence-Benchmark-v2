def insert_before_character(s):
    new_str = ''
    for char in s:
        if char == '5':
            new_str += 'h5'
        else:
            new_str += char
    return new_str