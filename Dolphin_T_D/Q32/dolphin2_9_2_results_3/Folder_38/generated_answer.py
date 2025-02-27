def insert_after_character(s):
    return ''.join(['6' if i == 'X' else i for i in s] + ['6' if s[-1] == 'X' else ''])