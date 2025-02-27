def insert_after_character(input_string):
    return input_string.replace('j', 'j' + 'q', 1) if input_string.count('j') else input_string