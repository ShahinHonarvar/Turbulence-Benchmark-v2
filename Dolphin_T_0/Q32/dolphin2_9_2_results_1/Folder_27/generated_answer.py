def insert_after_character(s):
    return ''.join((i + 'j' if i == 'N' else i for i in s))