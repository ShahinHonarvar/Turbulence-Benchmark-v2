def insert_after_character(string):
    return ''.join(['A' if i + 1 == j else s for i, s in enumerate(string) for j in range(len(string)) if s == 'A'])