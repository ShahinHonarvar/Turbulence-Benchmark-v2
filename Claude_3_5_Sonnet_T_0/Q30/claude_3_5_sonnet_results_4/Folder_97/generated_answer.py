def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'o':
            result += 'h'
        result += char
    return result