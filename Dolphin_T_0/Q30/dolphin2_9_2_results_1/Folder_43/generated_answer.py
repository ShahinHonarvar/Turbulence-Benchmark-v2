def insert_before_character(s):
    return 'G' + s if s[0] == 't' else s[0] + 'G' if s[1] == 't' else s[0] + insert_before_character(s[1:]) if s else ''