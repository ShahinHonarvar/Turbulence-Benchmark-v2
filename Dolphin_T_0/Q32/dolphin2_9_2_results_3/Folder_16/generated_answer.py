def insert_after_character(s):
    return_str = ''
    for char in s:
        if char == 'w':
            return_str += char + 'n'
        else:
            return_str += char
    return return_str