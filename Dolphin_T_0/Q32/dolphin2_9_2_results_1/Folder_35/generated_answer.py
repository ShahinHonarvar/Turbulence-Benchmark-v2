def insert_after_character(s):
    return ''.join([i + 'M' if i == '9' else i for i in s])