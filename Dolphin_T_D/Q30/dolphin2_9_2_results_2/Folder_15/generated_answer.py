def insert_before_character(s):
    return 'o'.join(('o' + s[i:] for i in range(len(s)) if s[i] == 'o'))