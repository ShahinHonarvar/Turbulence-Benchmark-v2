def insert_before_character(string):
    return ''.join(('V' if i == 'R' else x for x in string))