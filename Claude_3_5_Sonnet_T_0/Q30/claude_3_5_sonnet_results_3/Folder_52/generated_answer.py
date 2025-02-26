def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'T':
            result += 'V'
        result += char
    return result