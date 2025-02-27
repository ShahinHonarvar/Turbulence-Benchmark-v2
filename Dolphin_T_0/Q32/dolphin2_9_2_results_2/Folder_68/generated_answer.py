def insert_after_character(string):
    return ''.join((i + '0' if i == 'i' else i for i in string))