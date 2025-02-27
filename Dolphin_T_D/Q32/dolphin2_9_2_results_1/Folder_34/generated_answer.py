def insert_after_character(s):
    return ''.join([a + 'a' if a == 'A' else a for a in s])