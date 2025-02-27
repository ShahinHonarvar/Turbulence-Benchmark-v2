def insert_after_character(input_string):
    modified_string = ''
    for i in range(len(input_string)):
        modified_string += input_string[i]
        if input_string[i] == 'X':
            modified_string += '6'
    return modified_string