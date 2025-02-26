def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'c':
            result += 'G'
        result += char
    return result