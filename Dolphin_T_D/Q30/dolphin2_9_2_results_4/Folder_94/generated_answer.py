def insert_before_character(string):
    return ''.join(('5' + s if s == ' ' else s for s in string))