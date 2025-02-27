def insert_after_character(str):
    return ''.join([i + 'h' if i == '9' else i for i in str])