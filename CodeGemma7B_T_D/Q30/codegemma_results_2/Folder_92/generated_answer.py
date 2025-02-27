def insert_before_character(input_string):
    result = ''
    for char in input_string:
        if char == 'a':
            result += 'a' + char
        else:
            result += char
    return result