def insert_after_character(s):
    return ''.join(list(('h' if j == '5' else j for i, j in enumerate(s))))