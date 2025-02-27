def insert_after_character(s):
    return ''.join([i + 'N' if i == 'B' else i for i in s])