def insert_before_character(str):
    return ''.join([char if char != 'C' else 'P' + char for char in str])