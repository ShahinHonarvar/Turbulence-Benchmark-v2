def insert_before_character(string):
    return 'O' + ''.join((char if char != 'o' else 'O' + char for char in string))