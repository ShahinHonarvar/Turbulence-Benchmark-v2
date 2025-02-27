def insert_before_character(s):
    new_string = ''
    for char in s:
        if char == 'a':
            new_string += '6a'
        else:
            new_string += char
    return new_string