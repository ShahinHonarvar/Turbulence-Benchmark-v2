def insert_after_character(string):
    return ''.join(('U' + s if s == 'U' else s for s in string))