def insert_after_character(string):
    new_string = []
    for char in string:
        if char == 'j':
            new_string.append(char + 'v')
        else:
            new_string.append(char)
    return ''.join(new_string)