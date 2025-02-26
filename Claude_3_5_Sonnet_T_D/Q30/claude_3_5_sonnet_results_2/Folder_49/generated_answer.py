def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'i':
            result += 'i'
        result += char
    return result