def insert_after_character(string):
    return ''.join(['Z' if i < len(string) - 1 and s == 'C' else s for i, s in enumerate(string)]) + 'Z' if string[-1] == 'C' else ''