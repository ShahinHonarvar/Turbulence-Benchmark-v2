def insert_before_character(input_str):
    result = ''
    for char in input_str:
        if char == 'i':
            result += '0i'
        else:
            result += char
    return result