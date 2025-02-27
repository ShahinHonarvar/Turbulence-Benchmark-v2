def insert_before_character(s):
    return 'P'.join(('C' + s if c == 'C' else s for c in s))