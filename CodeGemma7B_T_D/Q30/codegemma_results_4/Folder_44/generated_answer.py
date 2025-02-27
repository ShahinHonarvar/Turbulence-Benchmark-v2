def insert_before_character(s):
    return ''.join([c if c != 'g' else 'M' + c for c in s])