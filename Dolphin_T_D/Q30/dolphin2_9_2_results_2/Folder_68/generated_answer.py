def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'i':
            result = result + '0' + char
        else:
            result = result + char
    return result