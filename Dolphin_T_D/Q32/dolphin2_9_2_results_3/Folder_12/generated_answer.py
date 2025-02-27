def insert_after_character(string):
    return ''.join(('I' + ' ' + c if c == 'I' else c for c in string))