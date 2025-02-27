def insert_after_character(string):
    return ''.join(['I' if i + 1 == j else string[j] for j, i in enumerate(string)])