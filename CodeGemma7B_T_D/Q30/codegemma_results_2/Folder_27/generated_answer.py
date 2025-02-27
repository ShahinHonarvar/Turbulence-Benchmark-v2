def insert_before_character(str_in):
    return ''.join([char for char, char_i in zip(str_in, str_in[1:]) if char != char_i or char_i == 'N'])