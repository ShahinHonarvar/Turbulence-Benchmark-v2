def insert_before_character(string):
    return 'n'.join(['H' if char == 'H' else '' for char in string]) + string