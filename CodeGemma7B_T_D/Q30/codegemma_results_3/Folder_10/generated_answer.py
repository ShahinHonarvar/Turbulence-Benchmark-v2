def insert_before_character(s):
    return ''.join([i + 'v' if i == 'j' else i for i in s])