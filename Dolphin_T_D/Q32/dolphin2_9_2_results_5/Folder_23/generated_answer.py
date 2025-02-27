def insert_after_character(input_string):
    return ''.join(list(('y' if input_string[i - 1] == 'b' and input_string[i] != ' ' else input_string[i] for i in range(1, len(input_string) + 1))))