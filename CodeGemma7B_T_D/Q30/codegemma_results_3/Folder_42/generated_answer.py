def insert_before_character(x):
    return ''.join((k + 'j' if k == 'O' else k for k in x))