def insert_before_character(s):
    return 'f'.join(('E' if i[0] == 'E' else i for i in s.split('E'))) + ('f' if s[-1] == 'E' else '')