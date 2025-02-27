def insert_after_character(s):
    return 'q'.join(('j' + i + 'q' if i != 'j' else i for i in s))