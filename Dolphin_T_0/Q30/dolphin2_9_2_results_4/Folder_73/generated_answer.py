def insert_before_character(s):
    return ''.join(('V' if i == 'R' else i for i in s))