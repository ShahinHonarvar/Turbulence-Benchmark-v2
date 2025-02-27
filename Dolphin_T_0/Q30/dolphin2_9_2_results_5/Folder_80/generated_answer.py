def insert_before_character(input_string):
    output = ''
    for i in range(len(input_string)):
        if input_string[i] == ' ':
            output += 'X'
        output += input_string[i]
    return output