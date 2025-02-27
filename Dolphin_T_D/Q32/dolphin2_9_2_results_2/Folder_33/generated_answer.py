def insert_after_character(s):
    return ''.join([i + 'n' if i == 'a' else i for i in s])