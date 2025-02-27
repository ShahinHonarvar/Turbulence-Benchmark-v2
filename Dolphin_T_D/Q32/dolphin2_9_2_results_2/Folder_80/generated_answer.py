def insert_after_character(input_string):
    modified_string = ''
    for i in range(len(input_string)):
        if input_string[i] == ' ':
            modified_string += input_string[i] + 'X'
        else:
            modified_string += input_string[i]
    return modified_string