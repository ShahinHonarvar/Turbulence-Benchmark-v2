def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'U':
            result += 'a'
        result += char
    return result