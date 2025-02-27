def insert_before_character(input_str):
    result = ''
    for char in input_str:
        if char == 'b':
            result += 'y'
        result += char
    return result