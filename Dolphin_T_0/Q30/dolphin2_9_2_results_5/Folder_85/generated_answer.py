def insert_before_character(string):
    return ''.join(('a' + i if i == 'o' else i for i in string))