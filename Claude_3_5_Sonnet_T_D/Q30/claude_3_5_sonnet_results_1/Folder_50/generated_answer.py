def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 't':
            result += 'u'
        result += char
    return result