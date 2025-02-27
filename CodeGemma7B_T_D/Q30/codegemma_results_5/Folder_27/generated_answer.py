def insert_before_character(str):
    return ''.join([char for char in str if char != 'N'] + ['j'] * str.count('N'))