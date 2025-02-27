def insert_after_character(string):
    return ' '.join(''.join((' ' if i % 2 == 1 else c for i, c in enumerate(string))).split())