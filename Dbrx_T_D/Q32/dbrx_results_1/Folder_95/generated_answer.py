def insert_after_character(input_string):
    return input_string.replace('j', 'j' + 'q', 1) if input_string.count('j') > 0 else input_string