def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'E':
            result += 'fE'
        else:
            result += char
    return result