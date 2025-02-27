def insert_after_character(s):
    return ''.join([i + 'I' if i == 'Q' else i for i in s])