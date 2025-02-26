def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'a':
            result += 'A'
        result += char
    return result