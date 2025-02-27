def insert_after_character(s):
    return ''.join(('f' if i != '' else i for i in s.replace('M', 'Mf')))