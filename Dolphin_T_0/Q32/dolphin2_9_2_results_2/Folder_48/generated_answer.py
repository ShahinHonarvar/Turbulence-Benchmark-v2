def insert_after_character(s):
    return ''.join([i + 'U' if i == 'S' else i for i in s])