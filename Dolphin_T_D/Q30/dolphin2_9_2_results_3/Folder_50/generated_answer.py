def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 't':
            result = result + 'u' + char
        else:
            result = result + char
    return result