def insert_after_character(s):
    return '0'.join(('e' + x if x.startswith('e') else x for x in s.split('e')))