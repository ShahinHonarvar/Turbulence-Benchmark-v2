def insert_after_character(s):
    return ''.join((x + 'F' if x == '4' else x for x in s))