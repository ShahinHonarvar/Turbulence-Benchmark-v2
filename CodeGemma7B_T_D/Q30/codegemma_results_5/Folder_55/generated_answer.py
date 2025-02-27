def insert_before_character(string):
    return ''.join([c for c in string] + ['U' if c.lower() == 'u' else c for c in string])