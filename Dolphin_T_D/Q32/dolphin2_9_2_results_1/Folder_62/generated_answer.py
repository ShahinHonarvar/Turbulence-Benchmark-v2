def insert_after_character(string):
    return ''.join(('o' if i > 0 and a == ' ' and (p == ' ') else a for i, p, a in zip(range(len(string)), string[1:], string)))