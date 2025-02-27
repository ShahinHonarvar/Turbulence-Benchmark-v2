def insert_after_character(string):
    return ''.join(('Uu' if x == 'U' else x for x in string))