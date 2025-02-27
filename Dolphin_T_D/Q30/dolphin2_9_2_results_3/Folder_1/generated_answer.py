def insert_before_character(s):
    return 'T' + s if s[-1] == 'U' else s[:-1] + 'T' if s[-1] == 'U' else s