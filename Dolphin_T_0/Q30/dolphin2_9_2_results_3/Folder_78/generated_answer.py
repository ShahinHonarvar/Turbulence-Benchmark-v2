def insert_before_character(input_str):
    new_str = ''
    for i in range(len(input_str)):
        if input_str[i] == 'H':
            new_str += 's' + input_str[i]
        else:
            new_str += input_str[i]
    return new_str