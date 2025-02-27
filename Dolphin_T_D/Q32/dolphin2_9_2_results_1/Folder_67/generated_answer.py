def insert_after_character(s):
    return ''.join([i + '1' if i == 'j' else i for i in s])