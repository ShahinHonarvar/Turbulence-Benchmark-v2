def insert_before_character(input_string):
    result = ''
    for i in input_string:
        if i == 'u':
            result += 'U'
        result += i
    return result