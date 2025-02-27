def insert_after_character(str):
    new_str = ''
    for char in str:
        if char == 't':
            new_str += char + 'u'
        else:
            new_str += char
    return new_str