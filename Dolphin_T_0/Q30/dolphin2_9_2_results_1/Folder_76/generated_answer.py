def insert_before_character(test_string):
    new_string = ''
    for char in test_string:
        if char == 'F':
            new_string += 'm' + char
        else:
            new_string += char
    return new_string