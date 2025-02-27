def insert_after_character(input_string):
    return input_string.replace('k', 'k' + 'k', 1) if input_string.count('k') > 1 else input_string