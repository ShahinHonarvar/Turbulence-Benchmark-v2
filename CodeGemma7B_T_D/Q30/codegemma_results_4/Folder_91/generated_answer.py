def insert_before_character(str):
    return ''.join([i if i != 'a' else '0' + i for i in str])