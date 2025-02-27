def insert_after_character(string):
    return ''.join(('e' if char.upper() == 'E' and i != len(string) - 1 else char for i, char in enumerate(string)))