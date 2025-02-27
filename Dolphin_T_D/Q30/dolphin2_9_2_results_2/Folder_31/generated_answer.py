def insert_before_character(string):
    return 'N'.join(('B' if char == 'B' else '' + char for char in string))