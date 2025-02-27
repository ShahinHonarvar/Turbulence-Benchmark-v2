def insert_before_character(s):
    return ''.join([x + 'a' if x == 'o' else x for x in s])