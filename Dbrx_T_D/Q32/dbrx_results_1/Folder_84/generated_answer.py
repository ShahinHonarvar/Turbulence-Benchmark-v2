def insert_after_character(input_string):
    return ''.join((letter if letter != 'H' else 'Hn' for letter in input_string))