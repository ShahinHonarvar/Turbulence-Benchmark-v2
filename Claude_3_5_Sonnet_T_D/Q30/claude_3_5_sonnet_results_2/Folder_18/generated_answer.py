def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'K':
            result += 'l'
        result += char
    return result