def insert_before_character(s):
    return 'M' + ''.join([c if c != 'g' else 'Mg' for c in s])