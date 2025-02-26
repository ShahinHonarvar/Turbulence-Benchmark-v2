def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'e':
            result += 'e'
        result += char
    return result