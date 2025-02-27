def insert_after_character(s):
    return ''.join(('j' if i == 'N' else i for i in s)) + 'N' if s[-1] == 'N' else ''