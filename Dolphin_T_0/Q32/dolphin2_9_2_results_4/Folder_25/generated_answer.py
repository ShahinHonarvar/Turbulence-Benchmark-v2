def insert_after_character(string):
    return 'W'.join(('e' + s + 'W' if s.endswith('e') else s + 'W' for s in string.split('W')))