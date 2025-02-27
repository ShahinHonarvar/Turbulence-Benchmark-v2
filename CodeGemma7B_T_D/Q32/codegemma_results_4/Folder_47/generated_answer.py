def insert_after_character(the_string):
    return ''.join((ch + 'f' if ch == 'E' else ch for ch in the_string))