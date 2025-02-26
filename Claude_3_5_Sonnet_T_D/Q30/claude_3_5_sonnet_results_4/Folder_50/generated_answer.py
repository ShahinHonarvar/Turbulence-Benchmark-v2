def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 't':
            result += 'ut'
        else:
            result += char
    return result