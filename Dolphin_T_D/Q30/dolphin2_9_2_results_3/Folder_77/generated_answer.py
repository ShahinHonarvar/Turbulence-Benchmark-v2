def insert_before_character(string):
    return 'h'.join(('9' + t if t == '9' else t for t in string))