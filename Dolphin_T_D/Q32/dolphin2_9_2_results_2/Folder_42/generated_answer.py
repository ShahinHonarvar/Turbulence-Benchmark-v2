def insert_after_character(s):
    return ''.join(('j' if i == 'O' else x for i, x in zip(s, s + 'j')))