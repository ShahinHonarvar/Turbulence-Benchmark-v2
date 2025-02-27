def insert_before_character(string):
    return 'd'.join([char if char != 'O' else 'd' + char for char in string])