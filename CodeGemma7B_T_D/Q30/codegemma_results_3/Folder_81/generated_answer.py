def insert_before_character(s):
    new_string = ''
    for char in s:
        if char == 'A':
            new_string += 'A' + char
        else:
            new_string += char
    return new_string