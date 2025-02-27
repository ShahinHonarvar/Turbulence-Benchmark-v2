def insert_after_character(s):
    s = s.split(' ')
    s = [' '.join(x) if y == '' else x for x, y in zip(s, s[1:] + [''])]
    return ' '.join(s)