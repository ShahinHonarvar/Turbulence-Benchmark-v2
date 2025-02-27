def insert_before_character(input_string):
    return 'o'.join(('o' + input_string[i] if input_string[i] == 'o' else input_string[i] for i in range(len(input_string))))