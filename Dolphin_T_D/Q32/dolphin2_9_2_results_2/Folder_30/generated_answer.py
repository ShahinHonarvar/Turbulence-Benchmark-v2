def insert_after_character(input_string):
    return 'F'.join([f'{i}F' if i == '4' else i for i in input_string])