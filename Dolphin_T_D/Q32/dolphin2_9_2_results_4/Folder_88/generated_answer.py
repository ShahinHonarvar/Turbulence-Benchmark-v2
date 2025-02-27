def insert_after_character(s):
    return ''.join((True if x == 'a' else x + 't' if x == 'a' else x for x in s))