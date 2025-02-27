def insert_before_character(s):
    return 'S'.join([i + ('' if i != '2' else 'S') for i in s])