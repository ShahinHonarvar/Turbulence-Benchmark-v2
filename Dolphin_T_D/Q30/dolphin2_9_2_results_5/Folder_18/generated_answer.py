def insert_before_character(s):
    return ''.join([x + 'l' if x == 'K' else x for x in s])