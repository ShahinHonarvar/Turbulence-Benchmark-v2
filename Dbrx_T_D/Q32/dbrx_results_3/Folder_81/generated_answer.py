def insert_after_character(input_string):
    return input_string.replace('A', 'A' + 'A' * (input_string.count('A') > 0), input_string.count('A'))