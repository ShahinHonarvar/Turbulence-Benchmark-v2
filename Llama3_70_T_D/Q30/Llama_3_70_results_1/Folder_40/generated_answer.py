def insert_before_character(s):
    new_string = ''
    for char in s:
        if char == 'e':
            new_string += 'e' + char
        else:
            new_string += char
    return new_string