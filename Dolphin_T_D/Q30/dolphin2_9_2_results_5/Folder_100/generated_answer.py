def insert_before_character(s):
    return ' '.join(('0' if i == '0' else '' if i == ' ' else i for i in s))