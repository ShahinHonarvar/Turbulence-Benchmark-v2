def insert_after_character(s):
    return ''.join([i + 'h' if i == '9' else i for i in s])