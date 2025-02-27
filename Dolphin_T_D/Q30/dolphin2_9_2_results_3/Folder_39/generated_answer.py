def insert_before_character(string):
    return 'Q'.join(('m' if c == 'm' else c for c in string if c != 'm'))