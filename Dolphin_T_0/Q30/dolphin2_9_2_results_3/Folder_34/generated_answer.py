def insert_before_character(string):
    return ''.join([s + 'a' if s == 'A' else s for s in string])