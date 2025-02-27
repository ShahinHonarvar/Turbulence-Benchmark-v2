def insert_after_character(s):
    return ''.join(('Hn' if char == 'H' else char for char in s))