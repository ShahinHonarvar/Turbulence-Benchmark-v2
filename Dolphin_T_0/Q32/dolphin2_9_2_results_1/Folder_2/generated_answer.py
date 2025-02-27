def insert_after_character(string):
    return ''.join(['Z' if j == 1 and i == 'C' else string[j - 1] for j, i in enumerate(string, 1)])