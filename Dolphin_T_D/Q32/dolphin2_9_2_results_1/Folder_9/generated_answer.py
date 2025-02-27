def insert_after_character(s):
    return ''.join([i + 'E' if i == 'e' else i for i in s])