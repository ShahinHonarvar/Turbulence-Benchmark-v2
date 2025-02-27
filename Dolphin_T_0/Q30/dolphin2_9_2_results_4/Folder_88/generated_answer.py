def insert_before_character(s):
    return 't' + s if s[0] == 'a' else s[0] + insert_before_character(s[1:]) if s else ''