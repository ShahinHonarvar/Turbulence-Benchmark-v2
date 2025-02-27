def insert_after_character(s):
    return ''.join([i + 'N' if i == 'm' else i for i in s])