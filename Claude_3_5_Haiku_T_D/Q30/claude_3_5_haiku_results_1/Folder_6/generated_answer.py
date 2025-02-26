def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'X':
            result += 'uX'
        else:
            result += char
    return result