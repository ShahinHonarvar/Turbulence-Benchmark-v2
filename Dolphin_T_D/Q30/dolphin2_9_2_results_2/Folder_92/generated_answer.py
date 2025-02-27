def insert_before_character(string):
    return 'a' + ''.join((a if a != 'a' else 'aa' for a in string))