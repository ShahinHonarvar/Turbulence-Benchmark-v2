def insert_before_character(s):
    new_string = ''
    for char in s:
        if char == 'u':
            new_string += 'U' + char
        else:
            new_string += char
    return new_string