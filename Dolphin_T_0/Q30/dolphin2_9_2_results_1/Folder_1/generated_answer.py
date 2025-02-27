def insert_before_character(string):
    return 'T'.join(('U' if char == 'U' else '' for char in string)).replace('U', '')