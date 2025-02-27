def insert_after_character(input_string):
    result = ''
    for i in range(len(input_string)):
        if i < len(input_string) - 1 and input_string[i] == 'O' and (input_string[i + 1] != 'O'):
            result += 'O' + input_string[i]
        else:
            result += input_string[i]
    return result