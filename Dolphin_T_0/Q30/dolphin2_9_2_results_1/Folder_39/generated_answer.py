def insert_before_character(input_string):
    result = ''
    for i in range(len(input_string)):
        if input_string[i] == 'm':
            result += 'Q'
        result += input_string[i]
    return result