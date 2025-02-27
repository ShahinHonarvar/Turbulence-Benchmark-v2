def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'C':
            result += 'H' + char
        else:
            result += char
    return result