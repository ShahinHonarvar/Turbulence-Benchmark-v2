def insert_before_character(text):
    return ''.join([c for c in text if c != 't'] + ['u'] + [c for c in text if c == 't'])