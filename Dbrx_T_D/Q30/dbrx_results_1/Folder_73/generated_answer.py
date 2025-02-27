def insert_before_character(input_string):
    result = ''
    for i in range(len(input_string)):
        if input_string[i] == 'R':
            result += 'V' + 'R'
        else:
            result += input_string[i]
    return result