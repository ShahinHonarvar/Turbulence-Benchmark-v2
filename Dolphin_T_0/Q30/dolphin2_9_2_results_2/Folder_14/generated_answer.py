def insert_before_character(s):
    return ' '.join((' ' + s[i:] for i in range(len(s)))).replace('  ', ' ')