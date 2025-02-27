def insert_after_character(s):
    return 'T'.join([x + 'T' if x == 'U' else x for x in s])