def insert_before_character(s):
    return 'f' + s if s[0] == 'M' else s[0] + insert_before_character(s[1:]) if s else ''