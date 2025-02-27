def insert_after_character(string):
    new_string = []
    for char in string:
        if char == 'K':
            new_string.append(char)
            new_string.append('l')
        else:
            new_string.append(char)
    return ''.join(new_string)