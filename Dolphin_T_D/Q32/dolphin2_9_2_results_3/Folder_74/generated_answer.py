def insert_after_character(str):
    return ' '.join(('T' + i[1:] if i[0] == 'T' else i for i in str.split(' ')))