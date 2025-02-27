def insert_before_character(s):
    return 'W' + s if s == ' ' else s[0] + 'W' + s[1:] if s[0] == ' ' else s[0] + insert_before_character(s[1:]) if s else ''