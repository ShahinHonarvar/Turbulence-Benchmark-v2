def insert_after_character(input_string):
    result = ''
    for char in input_string:
        result += char
        if char == 'a':
            result += 'W'
    return result