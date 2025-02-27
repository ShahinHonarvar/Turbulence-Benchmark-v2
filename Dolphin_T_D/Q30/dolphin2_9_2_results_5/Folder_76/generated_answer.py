def insert_before_character(s):
    return 'm' + s if s[0] == 'F' else s[0] + insert_before_character(s[1:]) if s else ''