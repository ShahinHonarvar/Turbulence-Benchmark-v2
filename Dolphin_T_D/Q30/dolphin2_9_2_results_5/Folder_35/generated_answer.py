def insert_before_character(input_string):
    result = ''
    for i in range(len(input_string)):
        if input_string[i] == '9':
            result += 'M9'
        else:
            result += input_string[i]
    return result