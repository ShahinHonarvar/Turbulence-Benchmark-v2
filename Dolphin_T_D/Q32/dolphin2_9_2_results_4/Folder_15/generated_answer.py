def insert_after_character(string):
    return ''.join(['o' if char == 'o' else char for char in string] + ['o'])