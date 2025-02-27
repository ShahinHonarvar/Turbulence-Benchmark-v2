def insert_before_character(input_string):
    return input_string.replace('0', '4' * ('0' in input_string) + '0')